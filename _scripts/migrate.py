#!/usr/bin/env python3
"""Migrate deep-learning-notes docs to Jekyll _research/ and _resources/ collections."""

import os
import re
from pathlib import Path

SRC = Path("/home/user/github/deep-learning-notes/docs")
DST_RESEARCH = Path("/home/user/github/CaoJiahao2.github.io/_research")
DST_RESOURCES = Path("/home/user/github/CaoJiahao2.github.io/_resources")

CATEGORY_TAGS = {
    "llm-mllm": ["大模型", "LLM", "MLLM"],
    "architectures": ["模型架构", "深度学习"],
    "training": ["训练技术", "深度学习"],
    "agents": ["AI Agent", "智能体"],
    "embodied-ai": ["具身智能", "机器人"],
    "deployment": ["模型部署", "推理优化"],
    "fundamentals": ["基础理论", "深度学习"],
}


def extract_title(content: str) -> str:
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return "Untitled"


def extract_description(content: str) -> str:
    lines = content.split("\n")
    found_h1 = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            found_h1 = True
            continue
        if found_h1:
            if not stripped:
                continue
            if stripped in ("---", "## 目录"):
                continue
            if stripped.startswith("> "):
                desc = stripped[2:].strip().strip("`").strip("*").strip()
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                return desc
            if stripped and not stripped.startswith("#") and not stripped.startswith("["):
                desc = stripped
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                return desc
    return ""


def generate_tags(category: str, title: str, is_resource: bool = False) -> list:
    if is_resource:
        return ["深度学习", "资源"]

    tags = ["深度学习", "科研笔记"]
    base_tags = CATEGORY_TAGS.get(category, [])
    tags.extend(base_tags)

    title_lower = title.lower()
    keyword_map = {
        "transformer": "Transformer", "cnn": "CNN", "rnn": "RNN",
        "lstm": "LSTM", "gan": "GAN", "diffusion": "Diffusion",
        "预训练": "预训练", "微调": "微调", "推理": "推理",
        "部署": "部署", "agent": "Agent", "智能体": "智能体",
        "vla": "VLA", "世界模型": "世界模型", "检测": "目标检测",
        "分割": "分割", "生成": "生成模型", "3d": "3D",
        "视频": "视频生成", "语音": "语音", "量化": "量化",
        "压缩": "模型压缩", "分布式": "分布式训练",
        "强化学习": "强化学习", "rlhf": "RLHF", "dpo": "DPO",
        "prompt": "提示工程", "rag": "RAG", "mcp": "MCP",
        "评测": "评测", "安全": "安全", "多模态": "多模态",
        "mllm": "MLLM", "推荐": "推荐系统", "flow": "Flow Matching",
        "深度": "单目深度", "优化": "优化器", "正则": "正则化",
        "反向传播": "反向传播", "分词": "Tokenizer",
        "代码": "代码智能", "可解释": "可解释性", "个性化": "个性化",
    }
    for kw, tag in keyword_map.items():
        if kw in title_lower and tag not in tags:
            tags.append(tag)

    return tags[:8]


def migrate_file(src_path: Path, dst_dir: Path, category: str, is_resource: bool = False):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    title = extract_title(content)
    description = extract_description(content)
    tags = generate_tags(category, title, is_resource)

    fm_lines = ["---"]
    fm_lines.append(f'title: "{title}"')
    if description:
        fm_lines.append(f'description: "{description}"')
    fm_lines.append("date: 2025-08-17")
    fm_lines.append(f"tags: [{', '.join(tags)}]")
    fm_lines.append("layout: single")
    fm_lines.append("author_profile: true")
    fm_lines.append("share: true")
    fm_lines.append("toc: true")
    fm_lines.append("comments: true")
    fm_lines.append("show_date: true")
    fm_lines.append("---")
    fm_lines.append("")

    front_matter = "\n".join(fm_lines)

    # Remove original H1 and blockquote to avoid duplication
    body_lines = content.split("\n")
    new_body = []
    found_h1 = False
    skipped_desc = False

    for line in body_lines:
        stripped = line.strip()

        if not found_h1:
            if stripped.startswith("# ") and not stripped.startswith("## "):
                found_h1 = True
                continue
            new_body.append(line)
            continue

        if found_h1 and not skipped_desc:
            if not stripped:
                continue
            if stripped in ("---", "## 目录", "## 目录 {#toc}"):
                skipped_desc = True
                new_body.append(line)
                continue
            if stripped.startswith("> "):
                continue
            skipped_desc = True
            new_body.append(line)
            continue

        new_body.append(line)

    body = "\n".join(new_body)

    stem = src_path.stem
    if is_resource:
        out_name = f"2025-08-17-{stem}.md"
    else:
        out_name = f"2025-08-17-{category}-{stem}.md"

    out_path = dst_dir / out_name

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(body)

    print(f"  OK  {out_name}  ({title})")
    return out_path


def main():
    gitkeep = DST_RESEARCH / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()
        print("Removed _research/.gitkeep")

    research_dirs = [
        "llm-mllm", "architectures", "training", "agents",
        "embodied-ai", "deployment", "fundamentals"
    ]

    total = 0
    for cat in research_dirs:
        cat_dir = SRC / cat
        if not cat_dir.exists():
            continue
        md_files = sorted(cat_dir.glob("*.md"))
        if not md_files:
            continue
        print(f"\n[{cat}] ({len(md_files)} files)")
        for f in md_files:
            migrate_file(f, DST_RESEARCH, cat)
            total += 1

    res_dir = SRC / "resources"
    if res_dir.exists():
        md_files = sorted(res_dir.glob("*.md"))
        if md_files:
            print(f"\n[resources] ({len(md_files)} files)")
            for f in md_files:
                migrate_file(f, DST_RESOURCES, "resources", is_resource=True)
                total += 1

    print(f"\nDone. Total migrated: {total} files")


if __name__ == "__main__":
    main()
