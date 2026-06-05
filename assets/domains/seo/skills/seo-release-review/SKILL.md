---
name: seo-release-review
description: "Use when reviewing a public SEO-oriented web project before claiming release readiness."
---

# SEO Release Review

## Checks

- Expected public URLs return successful status codes.
- Important pages have title, description, h1, body content, canonical URL, and language.
- `robots.txt` does not block intended public pages.
- `sitemap.xml` includes intended indexable URLs.
- Structured data is valid for the content type and does not make unsupported claims.
- Internal links expose important public pages.
- No preview, staging, or private pages are indexable.
- Search Console follow-up actions are documented when production exists.

## Output

Write findings with status, URL, evidence, and recommendation. Do not claim readiness while FAIL findings remain.
