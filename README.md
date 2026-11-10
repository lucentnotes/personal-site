# 个人网站：工作 Log

正式站点：https://lucentnotes.github.io/personal-site/

当前仅发布一篇工作 Log：**产品被认可之后，谁负责让它起作用？** 首页直接展示全文，暂不发布个人首页、项目列表或其他案例。

## 正式站点构建

```sh
npm run build:site
npm run preview:site
```

构建只需 Python 3；无需安装前端依赖。输出目录为 `site-dist/`，预览端口为 4173。将该目录完整同步到 `gh-pages` 根目录即可发布。

## 修改内容

- `public/work-log/index.html`：正文与结构。
- `public/work-log/style.css`：绿色视觉、正文与图形的统一阅读边界、响应式展示。
- `public/work-log/page.js`：界面对照、连续路径、动画播放与图片放大。
- `public/work-log/assets/`：原素材的已确认处理版本与标记为方案示意的目标界面。
- `scripts/build_work_log_site.py`：单页正式发布构建。

旧的 `/work-log/` 链接会跳转到根地址。正文、箭头关系、原界面完整比例和无水印素材保持已确认版本。

## 历史开发内容

原 React/Vite 首页、案例和审阅文档保留在仓库中，供后续参考，不属于当前正式站点。旧的 `npm run build` 和离线预览命令用于历史开发，不能作为正式发布产物。

发布范围与操作细节见 [正式站点说明](docs/production-site.md)。
