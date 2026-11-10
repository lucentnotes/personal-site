# 正式站点

入口：https://lucentnotes.github.io/personal-site/professional-insights/

发布范围为中英文各一个入口页和四篇独立文章页，共十页。默认入口为英文；中文版位于 `/professional-insights/zh/`。根路径与 `/work-log/` 始终跳转到英文入口。旧工作 Log 和其他历史页面不在发布产物中。

## 发布

1. `npm run build:site` 从最终 Markdown 生成页面并输出 `site-dist/`。
2. 本地检查正文、目录、图片、返回列表和上一篇／下一篇导航。
3. 将 `site-dist/` 完整同步到 GitHub Pages 的 `gh-pages` 分支根目录，移除产物之外的旧页面与资源。
4. 推送后验证正式入口、四个文章直达链接及旧地址跳转。

文章路由均为目录下独立的 `index.html`，可直接打开、刷新，不依赖服务器端路由或 JavaScript。图片保持原比例；家长期待篇保留 AI 插图标注。目录脚本只增强当前章节提示，禁用 JavaScript 仍可阅读和导航。

中英文切换为真实链接，跳转到同一篇文章的对应语言版本；章节锚点保持一致。目录、返回列表、上下篇、图片说明和放大界面随语言本地化。语言不写入浏览器偏好，也不根据浏览器语言自动跳转，因此正常分享默认入口仍显示英文。两种语言共用素材，不重复存储视频。

GitHub Pages 的 HTML 缓存可保留 10 分钟。构建会根据正文、排版和生成脚本计算发布版本，将该版本统一用于入口、卡片、返回列表、上一篇／下一篇和 CSS/JS 地址；根路径及旧 Log 的跳转也指向同一版本。不得只为临时直达链接手动加参数，而让站内导航落回旧的缓存地址。

导航回归检查：`python3 -m unittest discover -s tests -p 'test_insights_navigation.py'`（先构建）。发布后还应从文章返回列表，再逐一点击卡片核对新增图片，而非仅验证直达文章地址。

英文正文来源：`content/professional-insights/Professional-Insights-Final.md`；中文译文来源：同目录的 `Professional-Insights-zh.md`。译文逐段对齐，不新增经历、数据或成果。入口及辅助文字按用户批准的精简配图版预览制作。首页和其他板块不另作设计。

历史源码与既有未提交改动应保留，不随此次发布混入正式产物。
