# 里面有人 / What Stays · 第一幕

独立分支：`art/inside-immersive`。作品全部位于 `artworks/inside/`，作品集原有页面与发布配置保持独立。

## 运行和构建

在仓库根目录运行 `python3 -m http.server 8000`，打开 `/artworks/inside/`；英文版为 `/artworks/inside/?lang=en`。也可运行 `python3 scripts/build_inside_site.py`，生成可部署的独立静态目录 `inside-dist/`。

`index.html` 是整屏正式入口；`immersive-preview.html` 是兼容此前链接的相同入口。冷蓝纸纹、衬线字、平面无五官剪影。幕次目录按交接稿列出八幕，目前只开放第一幕，其余显示“待续”。每次刷新或通过浏览器历史重新进入，都返回封面和 0 秒，不恢复上次进度。

## 观看交互

- 点击“第一幕 / 离开”开始；空格暂停或继续，左右方向键前后五秒。
- 左下角倍速菜单默认收起，提供 1.25x、1.5x、2x；再次选择当前档位恢复 1x。字幕、动作、配乐同步加速；配乐使用保持音高的预处理音轨。
- 打开幕次目录暂停当前播放，关闭后恢复。可用 Tab、Enter、Escape 操作。
- 最后拖动窗上反光或操作滑杆，过界后转到另一个地方。交互等待期间配乐继续，完成后渐弱退出。
- 静置时轻量导航和控制项淡出；指针移动或键盘操作时出现。

## 本版画面

玻璃倒影里，女主旁的男影在约七秒内逐渐消散。出店后的锁屏时间随手指上滑、松手回弹，持机左手不伸出手指；滑动完成后停留六秒。舞会初始灯光较暗、人群清楚可见，随后人群散去、灯光亮起；男主走来坐下，触颈准备亲吻时配乐从曲头第一声进入。

## 文本、声音和资源

`timing.json` 是逐句中英文字幕的权威时间表，`timing.js` 为浏览器版本。以 handoff (4) 的开头和结尾为基础，保留后续用户确认的删句、分句和停留。两种语言共用 39 条字幕、187 秒固定时间线，末尾交互等待不计时。`film.js` 中的动作与拟音时间点随字幕统一计算。

当前没有人声旁白。环境与拟音由 Web Audio 本地合成，包括雨声、倒饭、碗底、脚步、行李轮、硬币、扫码、纸袋、打字、衣料、落座和舞会声场。`assets/inside-piano.mp3` 为自编钢琴循环；默认音量 24%，出便利店后完全淡出，舞会触颈时从 0:00 恢复。

钢琴渲染脚本为 `tools/render_score.py`，使用 FluidSynth 和系统 TimGM6mb piano。音色来源：Tim Brechbill (2004)、David Bolton (2010)，TimGM6mb SoundFont（GPL-2；未分发完整 SoundFont）。[原始音色记录](https://github.com/musescore/musescore-old/commit/90c33ef9d87b3f5ff92efd3b07d89eb455fb1fef)。`tools/render_speed_scores.py` 使用 FFmpeg atempo 生成三档保持音高的配乐。

`tools/package.py` 生成中英文离线单文件、SRT 和当前交付压缩包。离线 HTML 内嵌全部运行代码和音轨，无需联网。

## 验证

`verification.json` 记录浏览器验证。检查包括中英文、三档真实播放速度、配乐播放位置与画面同步、配乐音高保持、折叠倍速菜单、八幕可用状态、手机布局、刷新/历史返回重置，以及关键画面的实际截图。`deliverables/Revision-17-Preview.html` 汇总本轮修改截图。

## 本轮界面精简

目录内已移除“第一幕 · 选择片段 / Act I · Scenes”和“每次重返这里，都从头开始 / Each return begins at the beginning.”。重新进入从头开始的行为保留。英文总标题、封面字体与幕名已按后续确认更新，见下节。

## 已确认名称与英文封面

英文总标题为 What Stays。封面采用本地托管 Cormorant Garamond Regular，What / Stays 两行，收紧行距和字距；入口为小号无衬线字。字体与 OFL 许可位于 assets/fonts/，离线文件内嵌字体与许可。

1. 空出来的位置 / A Place Left Empty
2. 纸上的房间 / A Room on Paper
3. 今晚别来 / Not Tonight
4. 他睡过的地方 / Where He Slept
5. 一床被子的距离 / Under One Quilt
6. 门外还在说话 / Voices Beyond the Door
7. 下周还来吗 / Next Week, Too?
8. 旧稿里的雨 / Rain on the Page

## 开场与舞会声音调整

配乐默认降至 24%，开场前三秒渐入，舞会触颈时仍从曲头第一声恢复。舞会初始新增轻微的无可辨词人群底声，随可见人群散去淡出。assets/ballroom-murmur.mp3 为本项目生成的多层语音共振合成底声，不包含对白或外部录音。

## 舞会人群声待选

已撤下此前合成人群声；动画暂不加载或播放该音轨。候选真实场景录音登记在 crowd-candidates.json，三段均已核对原页面的 CC0 标注。等待用户选择 A/B/C 后再剪辑、调音量并接入。配乐 24% 与开场三秒渐入保持。
