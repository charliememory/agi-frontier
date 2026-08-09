---
hide:
  - navigation
  - toc
---

<div class="frontier-hero">
  <div>
    <p class="frontier-kicker">AGI Frontier / 研究实验室手册</p>
    <h1>从预测 token，走向能自我改进的系统。</h1>
    <p>一套公开、可复现、持续更新的 tutorial：梳理 LLM、多模态模型、生成模型、世界模型、VLA 与 self-improving agents 的共同脉络。</p>
    <div class="frontier-actions">
      <a href="tutorials/">开始阅读</a>
      <a href="experiments/">查看实验</a>
      <a href="https://github.com/charliememory/agi-frontier" rel="noopener">GitHub ↗</a>
    </div>
  </div>
  <aside class="frontier-brief">
    <strong>Working thesis</strong>
    AGI 的关键不只是更大的模型，而是表示、预测、反馈与闭环自改进逐步汇合。
  </aside>
</div>

## 一张正在生长的地图

<div class="frontier-map" markdown>
  <a class="frontier-node" href="map/">
    <small>01 · REPRESENT</small>
    <strong>表示世界</strong>
    <span>文本、图像、视频、状态与动作如何进入模型。</span>
  </a>
  <a class="frontier-node" href="timeline/">
    <small>02 · PREDICT</small>
    <strong>预测未来</strong>
    <span>token、latent、轨迹与动作预测的共同结构。</span>
  </a>
  <a class="frontier-node" href="radar/">
    <small>03 · VERIFY</small>
    <strong>获得反馈</strong>
    <span>从标签和偏好，到 verifier、奖励与环境反馈。</span>
  </a>
  <a class="frontier-node" href="radar/open-problems/">
    <small>04 · EVOLVE</small>
    <strong>持续变强</strong>
    <span>任务、数据、策略、代码和架构的自动改进。</span>
  </a>
</div>

## 当前状态

<div class="frontier-status">
  <div><b>主线</b><span>World models · VLA · Verifiers</span></div>
  <div><b>方法</b><span>读论文 → 跑最小实验 → 记录失败</span></div>
  <div><b>节奏</b><span>公开更新，保留判断变化</span></div>
</div>

## 如何使用这个站点

如果你是第一次来，从[能力地图](map/index.md)建立总览，再按[技术时间线](timeline/index.md)回看历史因果。Tutorial 不追求覆盖所有论文，而是每次选一个机制，写出最小实现，记录它解决了什么、在哪里失败、下一步如何验证。

研究者可以直接进入 [Frontier Radar](radar/index.md)，查看当前判断和开放问题；工程师可以从 [Experiments](experiments/index.md) 开始。站点内容以 GitHub 上的 Markdown 为事实来源，更新记录和修正也公开保留。

> **订阅更新**：第一阶段使用 GitHub Watch。RSS/Atom 与邮件订阅会在形成稳定内容节奏后再接入，不把额外运营系统变成学习负担。

## 一句话承诺

不维护“我读过什么”，而维护“我的 AGI 判断发生了什么变化，以及下一步如何验证”。
