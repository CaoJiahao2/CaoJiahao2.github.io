---
title: Cao Jiahao - Resume
description: Resume of Cao Jiahao, Master's student in Software Engineering at HUST, focusing on multimodal large language models, AIGC, computer vision, and AI application development.
date: 2025-07-01
permalink: /about-en/
tags: [resume, multimodal LLM, AIGC, computer vision, AI applications]
---

<p style="text-align:center;font-size:1.1rem;color:#888;">
  <a href="/about/">中文版 / Chinese Version</a>
</p>

<div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: flex-start; justify-content: space-between; margin: 1.5rem 0;">
  <div>
    <p><strong>Phone / WeChat:</strong> 18273523582</p>
    <p><strong>Email:</strong> <a href="mailto:caojiahao@hust.edu.cn">caojiahao@hust.edu.cn</a></p>
    <p><strong>Age:</strong> 23</p>
    <p><strong>Expertise:</strong> LLM / CV / AIGC Algorithm Engineer</p>
  </div>
  <img src="/assets/images/profile.jpg" alt="Cao Jiahao" width="220" height="293" loading="lazy" decoding="async">
</div>

## Education

### Huazhong University of Science and Technology (HUST, 985) · Software Engineering (A+ Discipline) · Vision & Feature Learning Lab · M.S. (Graduate without Entrance Exam)
*2024.09 – 2027.06*

- **Supervisor:** Prof. Bai Xiang (National Science Fund for Distinguished Young Scholars, IEEE Fellow)
- **Research Interests:** Multimodal LLM, AIGC, Computer Vision, AI Application Development

### Huazhong University of Science and Technology (HUST, 985) · Intelligent Construction (Minor in Computer Science) · Excellent Engineer Program Pilot Class · B.E.
*2020.09 – 2024.06*

- **Comprehensive Ranking:** 5/82
- **Honors:** HUST Outstanding Undergraduate (top ~3%), First-class Scholarship for Scientific & Technological Innovation, Academic Excellence Scholarship, etc.

## Internship Experience

### Turing Artificial Intelligence Research Institute (Nanjing) · Vision Algorithm Engineer
*2026.06 – Present*

#### General Industrial Defect Detection LLM
*Tech stack: Multimodal VLM / LoRA Fine-tuning / vLLM Deployment*

- **Background:** Traditional industrial quality inspection requires training a separate model per product, with poor generalization and high iteration cost. Built a general defect detection system covering **7 industrial domains** (footwear, apparel, PCB, etc.) based on the **Qwen3.5-4B** VLM, using one shared backbone + multi-domain LoRA for cross-domain reuse and efficient deployment.
- **Training pipeline:**
  - Data layer: normalized 7 industrial datasets with a unified annotation format and a bbox coordinate normalization pipeline to [0, 1000].
  - **SFT stage:** three-stage **progressive training** — Stage 1 learns bounding-box localization only, Stage 2 introduces defect classification, Stage 3 injects domain-specific defect priors (e.g., "snags, oil stains, pilling" for apparel), gradually increasing task complexity.
  - **DPO stage:** built three types of preference pairs (false-positive suppression, false-negative suppression, localization quality) to further refine the model's defect-judgment boundary.
- **Engineering & deployment:** single-GPU multi-LoRA residency via vLLM with **request-level millisecond hot-switching (<10ms)** through in-place weight add/subtract (~500MB VRAM for 7 adapters); designed a complete post-processing pipeline of tiled inference + aggregation + NMS to improve small-target detection.
- **Results:** metal-domain mIoU improved from 0.11 to **0.50 (+4.4×)**; medical-device Precision reached **70.6%**; 7 domains share one backbone with <10ms switching and 1-2s per-image inference, meeting real-time production-line requirements.

#### Foam Detection & Consistency Quantification System Based on SAM
*Tech stack: Vision Foundation Model / PEFT*

- **Background:** for foam quality assessment in the daily-chemical industry, built an end-to-end automated evaluation system (arm segmentation → foam instance segmentation → consistency quantification) based on the **SAM3.1 (~850M)** vision foundation model, replacing manual scoring.
- **Parameter-efficient fine-tuning:** injected LoRA (rank=16) into the ViT Backbone, DETR Encoder/Decoder, and Mask Decoder for a small dataset (500 labeled samples); only ~**11M trainable parameters (1.3% of the base model)**; designed an online augmentation pipeline (flip/rotate/crop/color jitter) improving foam-segmentation F1@0.50 by ~**18%** over zero-shot.
- **Multi-factor consistency quantification:** a three-factor fusion scoring model — geometric (coverage + fill ratio), photometric (foam-skin brightness difference + whiteness ratio), and textural (multi-scale bubble detection + density/uniformity) — outputs L1~L5 levels with **85%+** agreement with human ratings.

## Research & Projects

### Vision Feature Enhancement MLLM for Underwater Scene Understanding
*Multimodal LLM · 2024.11 – 2025.04*

- **Background:** built a multimodal understanding framework on LLaVA-1.5 / Qwen2.5-VL for degraded underwater scenes (low light, turbidity, color cast), covering **8 task types** (coarse/fine classification, detection, counting, referring localization, image captioning, VQA) with **unified instruction interaction** at image/region/object level.
- **Data engineering:** assembled public underwater datasets into ~**158K images / 1.45M image-text QA** instruction pairs; designed rule-based template generation for detection/classification tasks and introduced MLLM-generated open-vocabulary labels with quality filtering and manual review.
- **Core method:** decomposed degradation into **backscatter interference + absorption attenuation** based on the underwater imaging model; located dark tokens via the lowest-average RGB patch, estimated the scattering response with **cross-attention**, and predicted absorption weights from depth features to recover degraded visual information in feature space.
- **Training results:** trained **LoRA (rank=128) + vision-language projection + visual feature enhancement** jointly on 4×A800-80GB; vs. a generic MLLM baseline, achieved **+5.6%** on classification and **+4.3** on Grounding PR@0.5, with stable gains on degraded subsets (low light, color cast).

### Multi-View Synchronized Image Generation System Based on FLUX
*Multimodal Generation / Diffusion Models · 2026.01 – 2026.04*

- **Background:** to address subject identity drift and local detail misalignment in multi-view generation by generic text-to-image models, built a multi-view synchronized generation system on **FLUX.1-dev (4B)** trained with UE-rendered multi-view data.
- **Multi-view synchronized modeling:** inserted a lightweight multi-view synchronization module into the FLUX Transformer, reorganizing image tokens across views with 12-D camera extrinsics and view positional encoding, enabling token-level cross-view interaction for joint global-semantic and local-detail modeling across N views.
- **Stable training strategy:** froze the FLUX.1-dev backbone and trained only the new modules on a single 4090-48G; used zero-initialized residual branches, intermittent sync-layer insertion, and single-view replication so the model starts close to the original output and gradually learns cross-view alignment.
- **Evaluation:** cross-view matched-point count improved ~**1.6×**, cross-view CLIP similarity improved **5%–8%**; CLIP-T remained stable and FID increase stayed within **10%**, with more consistent local details across images.

## Skills

- Proficient in **Python, C/C++** and AI frameworks including **swift, transformers, diffusers, ollama, LangChain**.
- Deep understanding of **multimodal alignment, LLM post-training, parameter fine-tuning, and model deployment**, with hands-on **AIGC/multimodal** project experience.
- Experienced with AI-assisted development tools such as Claude Code, Codex, and Cursor; closely following **AI agents, embodied AI, and RL**.

## Competitions

- 18th "Challenge Cup" Special Track (Smart Robot for Urban Drainage Pipeline Operations) — **Top Finalist (擂主)** · 2023.09
- 22nd "Huawei Cup" China Graduate Mathematical Contest in Modeling — **National Second Prize** · 2025.09

<p style="text-align:center;margin-top:2rem;color:#888;">Feel free to reach out via email or WeChat — I'm always happy to connect!</p>
