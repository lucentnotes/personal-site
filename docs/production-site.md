# 正式站点

正式地址：https://suojin311-creator.github.io/personal-site/

目前唯一内容为已确认的工作 Log。没有独立首页或其他项目页。旧的 `/work-log/` 地址仅跳转到根地址，保留查询参数和锚点。

## 内容与构建

- 页面源码：`public/work-log/`。
- 构建命令：`npm run build:site`。
- 发布产物：`site-dist/`。它仅复制工作 Log 与其资源，不复制 `public/` 下的历史草稿。
- 本地检查：`npm run preview:site`。
- GitHub Pages：`gh-pages` 分支根目录。

更新正式站点时，应将 `site-dist/` 完整同步到发布分支，移除不在产物中的历史页面。不要使用旧版 React/Vite 构建或离线审阅包覆盖正式站点。

历史首页、成长包案例、视觉探索和文档在源码及 Git 历史中保留，未随本次正式站点发布。既有未提交的历史开发改动不属于本次发布。
