# Professional Insights

正式入口：https://suojin311-creator.github.io/eportfolio/professional-insights/

当前发布中英文各一个入口页和四个独立文章页。默认英文，所有页面右上角均可切换语言；中文版位于 `/professional-insights/zh/`。切换对应到同一篇文章，返回列表和上下篇导航保持当前语言。根地址和旧 `/work-log/` 链接始终跳转到英文入口，不按浏览器语言或历史选择自动切换。

## 构建与预览

```sh
npm run build:site
npm run preview:site
```

只需 Python 3；产物为 `site-dist/`，本地预览端口 4173。将产物完整同步到 `gh-pages` 根目录发布。

## 内容来源

- `content/professional-insights/Professional-Insights-Final.md`：用户提供的四篇最终正文，保持原文。
- `content/professional-insights/Professional-Insights-zh.md`：逐段对齐的中文译文，保留原文的职责、观察和验证边界。
- `content/professional-insights/cards.json`：原型中的文章分类。
- `scripts/build_professional_insights.py`：生成中英文共十个独立页面，共用图片、视频和样式。
- `public/professional-insights/`：生成页面、样式、阅读目录脚本、主题标志和三张选定图片。
- `scripts/build_professional_insights_site.py`：正式发布打包与旧链接跳转。

家长期待篇的场景图为用户指定的 AI 插图，页面保留标注。展会及玩具店图片为用户提供的实拍。未使用其他 AI 模拟实景图。

第一篇仅补充场景模拟与数字人阿乐老师两张实际界面，完整展示并支持放大。第三篇的习惯养成助手段落附产品刷牙动画，点击播放，不自动播放或预加载视频。相关素材在 `public/professional-insights/media/`。

第二篇的家长操作负担段落配成长中心；第三篇的产品定位段落配动画内容与详情页；第四篇的产品价值传达段落配商城界面。六张界面按各自上下文分布，均保留完整比例。

历史 React/Vite 页面和旧工作 Log 保留在源码中，不属于当前正式发布内容。不要用旧 `npm run build` 的产物覆盖正式站点。详见 [发布说明](docs/production-site.md)。
