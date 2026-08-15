# CaoJiahao2.github.io — 个人主页

Cao Jiahao 的个人主页，基于 [Jekyll](https://jekyllrb.com/) 与 [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) 主题构建，通过 GitHub Pages 部署。

## 站点结构

站点包含以下主要栏目（导航栏入口）：

- **首页** `/` —— 欢迎语与最新文章列表
- **博客** `/blog/` —— 全部博客文章（`_posts/`）
- **观点** `/idea/` —— 观点集合（`_idea/`）
- **资源** `/resources/` —— 资源集合（`_resources/`）
- **科研** `/research/` —— 科研集合（`_research/`）
- **生活** `/life/` —— 生活集合（`_life/`）
- **光影** `/photography/` —— 摄影集合（`_photography/`）
- **关于我** `/about/` —— 中文简历，另有 `/about-en/` 英文版

## 本地构建

本地使用与 GitHub Pages 一致的环境（通过 `github-pages` gem）：

```bash
bundle install
bundle exec jekyll serve   # 本地预览 http://127.0.0.1:4000
bundle exec jekyll build   # 构建到 _site/
```

### 常见问题

- 安装依赖较慢时，可参照 GitHub 官方文档配置 Ruby 与 Bundler。
- 若 gem 安装失败，尝试 `bundle update` 或更换镜像源。

## 如何新增内容

- **博客文章**：在 `_posts/` 下新建 `YYYY-MM-DD-slug.md`，front matter 参考现有文章（`layout: single`、`categories`、`tags` 等）。
- **集合文章**：在对应集合目录（如 `_research/`、`_life/`）下新建文档，front matter 参考 `_resources/2025-07-02-resources.md`。
- **页面**：在 `_pages/` 下新建 `.md`，通过 `permalink` 控制访问路径。

## 配置说明

- 站点元信息、导航、评论、搜索等均在 `_config.yml` 中配置。
- **评论（Giscus）**：评论使用 Giscus，需先在仓库启用 Discussions，然后在 [giscus.app](https://giscus.app) 生成 `repo_id` / `category_id`，填入 `_config.yml` 的 `comments.giscus` 对应字段。
- **搜索**：站内搜索为轻量自定义方案，索引由 Jekyll 在构建时生成于 `/search.json`，支持中文匹配。

## 部署

推送 `master`（或 `main`）分支后，GitHub 自动通过 GitHub Pages 构建并发布。仓库设置中的 Pages 需指向正确的分支与目录（通常为 `/ (root)`）。

## 目录速览

```
_pages/       页面（关于、科研、生活、光影等）
_posts/       博客文章
_idea/        观点集合
_resources/   资源集合
_research/    科研集合（待补充内容）
_life/        生活集合（待补充内容）
_photography/ 摄影集合（待补充内容）
_includes/    主题组件
_layouts/     页面布局
_sass/        Sass 样式
assets/       图片、CSS、JS 资源
```

## 许可

个人主页内容归作者所有；主题代码基于 [MIT License](LICENSE) 的 Minimal Mistakes。
