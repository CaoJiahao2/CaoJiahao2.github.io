# Repository Guidelines

Contributor guide for **CaoJiahao2.github.io**, a personal website built with [Jekyll](https://jekyllrb.com/) and the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, deployed via GitHub Pages.

## Project Structure & Module Organization

- `_posts/` — blog articles, named `YYYY-MM-DD-slug.md`
- `_pages/` — standalone pages (`about.md`, `search.md`) with a `permalink` front-matter field
- `_idea/`, `_resources/`, `_research/`, `_life/`, `_photography/` — Jekyll collections for each navigation section
- `_data/` — site data (`navigation.yml`, `authors.yml`, `ui-text.yml`)
- `_config.yml` — site metadata, navigation, search, and comment settings
- `_includes/`, `_layouts/`, `_sass/` — theme components and styles
- `assets/` — images, CSS, and JS
- `_site/` — generated build output (gitignored)

## Build, Test, and Development Commands

Uses Ruby + Bundler with the `github-pages` gem for parity with GitHub Pages.

```bash
bundle install            # install dependencies (Gemfile)
bundle exec jekyll serve  # local preview at http://127.0.0.1:4000
bundle exec jekyll build  # generate the site into _site/
```

There is no test suite. Verify new content locally with `bundle exec jekyll serve`.

## Coding Style & Naming Conventions

- Content uses YAML front matter: `title`, `categories`, `tags`, and `date` for posts; `permalink` for pages
- Follow existing files (e.g., `_resources/2025-07-02-resources.md`) when adding collection entries
- Posts and dated collections use `YYYY-MM-DD-slug.md`; slugs are lowercase with hyphens
- Keep `_config.yml` settings commented; restart the server after editing it
- No linters are configured; use 2-space indentation for YAML and follow existing Markdown style

## Testing Guidelines

Automated tests are not used. Validate changes by:

1. Running `bundle exec jekyll build` and confirming it exits cleanly
2. Serving locally and checking the affected pages and links
3. Confirming `/search.json` regenerates when content is added

## Commit & Pull Request Guidelines

- Commit messages are short and imperative; recent history is in Chinese (e.g., `fix bug on right`, `新增搜索功能`). Match the language of the change
- Create a descriptive branch off `master` before opening a PR
- Fill out `.github/PULL_REQUEST_TEMPLATE.md`; note whether the change is a bug fix, feature, or content addition
- Reference related issues and include screenshots for visual changes
- Push to `master`; GitHub Pages builds and deploys automatically

## Security & Configuration Tips

- Never commit real API keys or tokens
- Giscus comments (`_config.yml` → `comments.giscus`) need a `repo_id` and `category_id` from [giscus.app](https://giscus.app); keep the `YOUR_GISCUS_*` placeholders until configured
- Preserve `.gitignore` entries for `_site/`, `.jekyll-cache`, and `Gemfile.lock`
