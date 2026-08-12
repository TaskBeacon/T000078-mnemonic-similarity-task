# 助记相似性任务：情景记忆精度、海马模式分离及其测量边界

情景记忆需要在保留共同语义的同时区分高度重叠的经历。传统再认测验主要比较学过项目与全新项目，命中率较高既可能来自精确的项目表征，也可能来自概略熟悉感，因而难以直接刻画相似记忆之间的干扰。助记相似性任务（Mnemonic Similarity Task, MST）在再认阶段加入与学习项目知觉相似但并不相同的诱饵，通过“旧—相似—新”判断将项目再认与助记辨别置于同一测量设计中。该范式常被用于研究海马模式分离（pattern separation）的行为表现，但任务得分同时受编码质量、知觉辨别、提取策略与反应标准影响。因而，MST 的方法学价值在于提供受控的相似性梯度和可分解的反应分布，而非把单一行为指标等同于某一神经计算（Yassa & Stark, 2011; Stark et al., 2019）。

## 1. 范式提出与理论背景

模式分离指把相似输入转换为较少重叠的表征，以降低新旧经历之间的干扰；互补的模式完成则允许部分线索恢复既有表征。海马计算模型长期将齿状回（dentate gyrus, DG）和 CA3 亚区置于二者平衡的核心。Kirwan 与 Stark（2007）以连续再认设计操纵项目相似性，并用高分辨率功能磁共振成像（functional magnetic resonance imaging, fMRI）考察内侧颞叶对重复项目、相似诱饵与新项目的响应，由此奠定了人类助记辨别范式的实验基础。随后，Stark 等（2013）将任务规范为更适合行为与临床研究的两个阶段：偶发编码后进行意外再认，测试项目等比例包含完全重复的目标、相似诱饵和未学习的新项目。该版本通常称为 MST，也曾称为行为模式分离任务。

从理论上看，诱饵判断提供了比普通新旧再认更高的表征精度要求。若诱饵保留目标的概略特征而缺少足够项目特异信息，参与者更可能选择“旧”；若能恢复二者的差异，则更可能选择“相似”或“新”。这一反应并非模式分离的直接读出。“相似”选项本身改变判断标准，正确拒绝诱饵还可能依赖回忆拒绝、熟悉性比较和测试后监控。MST 因此把海马计算理论转化为可检验的行为假设，同时保留了对其他认知过程的敏感性（Morcom, 2015; Stark et al., 2019）。

## 2. 任务逻辑、流程与核心指标

经典两阶段版本在编码期呈现日常物体图片，参与者判断物体通常位于室内还是室外。该任务与随后的记忆测验在表面要求上不同，可降低有意背诵策略的支配作用。测试期随机混合三类项目：目标是学习图片的完全重复；诱饵与某个学习项目属于同一物体对，但在形状、视角或细节上不同；箔项（foil）未在编码期出现。参与者分别作“旧”“相似”“新”判断，通常不提供逐试次正确性反馈。完整标准版本常采用 128 个编码项目与 192 个测试项目，其中目标、诱饵和箔项各 64 个；具体呈现时长和编码—测试间隔在不同研究中有所调整（Stark et al., 2013, 2019）。

主要指标为诱饵辨别指数（Lure Discrimination Index, LDI）：

\[
LDI=P(\text{相似}\mid\text{诱饵})-P(\text{相似}\mid\text{箔项})。
\]

减去箔项上的“相似”反应旨在校正个体使用该按键的一般倾向。校正再认指数则为：

\[
REC=P(\text{旧}\mid\text{目标})-P(\text{旧}\mid\text{箔项})。
\]

LDI 主要对应相似项目之间的助记辨别，REC 主要对应传统项目再认。二者的分离使研究者能够检验某一因素是否选择性影响记忆精度。标准刺激集还依据诱饵与目标的经验相似度划分若干等级；诱饵相似度越高，误报为“旧”的概率通常越大，因此完整的条件×反应矩阵和相似度函数比单一总分保留更多信息（Stark et al., 2019; Ma & Zhang, 2025）。基线版本通常预先平衡条件和相似度等级，不使用依据在线表现改变难度的自适应程序。

## 3. 主要行为与神经科学发现

### 3.1 助记辨别、老化与记忆精度

健康老化和遗忘型轻度认知障碍（amnestic mild cognitive impairment, aMCI）研究显示，年龄或认知状态对 LDI 的影响可大于对 REC 的影响，支持助记辨别相对于普通再认的增量敏感性（Yassa et al., 2011; Stark et al., 2013）。这种群体差异不能解释为纯粹的海马模式分离缺陷。编码注意、视觉敏锐度、执行控制和反应策略均可改变诱饵反应；较新的老年样本研究发现，执行功能能够解释部分 LDI 个体差异（Jensen et al., 2023）。因此，年龄组比较应同时报告 REC、视知觉与一般认知控制指标，并检查诱饵相似度梯度，而不宜把低 LDI 直接视为海马病理的特异标志。

助记辨别也与更广义的表征精度有关。Xie 等（2025）发现 MST 诱饵辨别与短时及长时记忆精度相关，提示该指标捕捉的并非仅是一次再认决策中的偏差。然而，相关关系仍不能确定共享方差源于海马表征、视觉精度还是一般记忆能力。对完整反应分布的认知建模进一步表明，经典 LDI 所隐含的测量假设未必能充分预测个体反应；在一个超过 150 人的数据集中，单维信号检测模型的拟合优于经典指标对应的模型（Ma & Zhang, 2025）。

### 3.2 fMRI 对内侧颞叶网络的约束

高分辨率 fMRI 证据较一致地表明，助记干扰的解决涉及 DG/CA3 及其内侧颞叶输入通路。原始连续再认研究观察到 DG/CA3 对输入变化表现出与模式分离相符的非线性响应，而 CA1 的响应更接近输入相似性的连续变化（Kirwan & Stark, 2007）。对象与空间版本的比较进一步显示，外侧与内侧内嗅皮层分别对对象和空间干扰呈现差异性参与，DG/CA3 则在两类干扰中均与辨别有关（Reagh & Yassa, 2014）。这些结果把任务效应置于分层的内侧颞叶网络中，而非单一“模式分离脑区”。

老化研究为脑—行为联系提供了更直接的证据。无痴呆老年人的助记辨别下降与 DG/CA3 活动增高相关（Yassa et al., 2011）；在对象辨别条件下，前外侧内嗅皮层活动降低、DG/CA3 活动增高及二者失衡又与行为缺陷相联系（Reagh et al., 2018）。fMRI 结果支持特定任务对内侧颞叶环路完整性的敏感性，但血氧水平依赖信号不能单独证明某亚区实施了因果性的模式分离计算。扫描版本在呈现时间、空间条件和分析对比上也常不同于标准两阶段行为 MST，跨研究推论应限定在共同的诱饵辨别操作上。

### 3.3 EEG 所揭示的提取时间进程

事件相关电位（event-related potential, ERP）研究表明，诱饵判断同时包含提取与提取后控制。Morcom（2015）发现，刺激后 500–800 ms，正确识别的目标和被误判为“旧”的诱饵均出现左侧中央顶区旧/新效应；800–1100 ms 的右侧额中央效应又随诱饵辨别能力而变化。该时间进程说明相似诱饵可引发对学习事件的错误回忆，并需要后续监控。它也提示“相似”反应不能被简化为早期知觉区分。头皮 ERP 对加工时序具有解释力，其空间定位不足以区分 DG、CA3 或内嗅皮层来源。

## 4. 范式发展与主要应用

MST 的发展主要沿着任务效率、远程施测和临床解释三条方向推进。缩短或连续呈现版本可减少时间负担，但反应选项、刺激数量和新旧比例的改变可能同时改变构念。Stark 等（2023）在多个实验中比较不同版本，传统全长“旧—相似—新”版本在剔除一个离群值后的 LDI 重测相关达到 .73；连续格式可以保留较好的可靠性，而改成简单“旧—新”判断会明显降低可靠性。这说明效率优化不能只依据平均组效应，还需检验个体排序的稳定性。后续大样本研究表明，优化版 MST 在现场与远程施测之间具有较高一致性，并可用于多种社区环境，但这一结论对应特定的自动化版本与施测控制（Azer et al., 2026）。

在临床研究中，MST 已用于老化、aMCI 与阿尔茨海默病风险评估。aMCI 的高分辨率 fMRI 研究显示，低剂量左乙拉西坦降低海马过度活动，并改善依赖 DG/CA3 的助记辨别表现，为神经活动与行为变化之间提供了干预性证据；该结果来自小样本、特定剂量和衍生扫描任务，不能直接推广为常规治疗效应（Bakker et al., 2012）。近期多项式加工树模型在 200 余名年轻人、健康老年人和 MCI 个体中，对认知状态及脑脊液淀粉样蛋白和磷酸化 tau 状态的区分优于传统分数（Vanderlip et al., 2024）。这项结果支持模型化指标的筛查潜力，但尚不足以把 MST 作为独立诊断工具。

## 5. 测量效度与解释边界

MST 具有明确的操作效度：目标、诱饵和箔项允许分别估计项目再认、相似项目辨别与反应偏向；诱饵相似度等级还可检验心理测量函数。其神经效度来自病灶、老化、高分辨率 fMRI 和干预研究的汇合，而不是某个单一脑区对比（Stark et al., 2019）。全长版本的重测表现适合群体研究和一定程度的个体差异分析，但信度依赖刺激集是否平行、重测间隔、反应格式与试次数（Stark et al., 2023）。

解释时至少需保留三项限制。第一，LDI 是两个比例之差，会把辨别能力与“相似”反应标准混合；只报告 LDI 可能掩盖“旧”“相似”“新”三类反应的不同来源（Ma & Zhang, 2025）。第二，室内/室外判断造成的编码差异、视觉质量、注意和执行功能都会影响后续诱饵反应（Jensen et al., 2023）。第三，稳定的群体效应不保证个体诊断准确，相关的脑—行为关系也不建立因果机制。研究设计宜预先规定主要指标，完整报告条件×反应矩阵、REC、反应时和漏答，并在需要个体预测时进行独立样本校准。

刺激与统计设计还决定效度能够维持到何种范围。高度相似诱饵可能造成地板效应，低相似诱饵则可能接近普通新项目；若年龄组或临床组在视觉辨别上已有差异，相同刺激等级并不必然代表相同的助记干扰。研究者宜在样本内检验相似度—反应函数，平衡各等级和项目类别，并避免在重复测量中直接复用全部图片。差值分数的方差也取决于两个组成比例及其协方差，试次数过少会降低个体估计稳定性。除预注册的 LDI 与 REC 外，可使用项目层级或信号检测模型分析完整反应分布，但模型选择、先验和外部验证应与传统指标分开报告（Stark et al., 2019, 2023; Ma & Zhang, 2025）。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
|---|---|---|---|
| 完整行为实验源码 | T000078 | PsychoPy/PsyFlow 本地实验实现 | [GitHub](https://github.com/TaskBeacon/T000078-mnemonic-similarity-task) |
| 行为型网页源码 | H000078 | 与完整行为流程配对的浏览器实现 | [GitHub](https://github.com/TaskBeacon/H000078-mnemonic-similarity-task) |
| 在线运行入口 | H000078 | 无采集硬件的浏览器运行版本 | [启动任务](https://taskbeacon.github.io/psyflow-web/?task=H000078-mnemonic-similarity-task) |

T000078 当前版本的采集类型为行为测量，语言为中文。配对 H000078 保留 128 个编码试次、192 个测试试次、同一刺激集和计分语义；它以浏览器事件替代本地硬件触发，由共享网页运行器管理显示与数据导出。该网页版本可用于行为体验和在线施测，不应被视为 EEG 或 MRI 采集版本。

### 6.2 实现流程与关键参数

![TaskBeacon 助记相似性任务流程](../task_flow.png)

**图 1. TaskBeacon 当前版本的试次流程。** 编码阶段随机呈现 128 张日常物体的 `a` 图，参与者在图片出现后的 2.0 s 内以 V/N 键判断“室内/室外”，随后为空白屏 0.5 s；系统不提供逐试次正确反馈。意外测试阶段随机呈现 64 个目标（编码时同一 `a` 图）、64 个诱饵（对应物体对的 `b` 图）和 64 个箔项（未编码的 `a` 图），参与者在 2.0 s 内按 V/B/N 分别报告“旧/相似/新”，随后为空白屏 0.5 s。诱饵从五个经验相似度等级中近似均衡抽取，目标、诱饵和箔项的项目编号互不重叠；固定随机种子 78078 预先生成并打乱两个阶段，不依据在线成绩调整难度。任务结束时反馈 LDI、REC、测试正确率、作答率和平均反应时。

该实现使用官方 Set 1 配对物体图片。编码阶段含 64 个未来目标和 64 个未来诱饵的基准图片；测试答案分别规定为目标“旧”、诱饵“相似”和箔项“新”。程序记录阶段、条件、配对编号、诱饵等级、按键、反应时、正确性与超时状态。LDI 与 REC 按前述公式计算，因而与标准两阶段 MST 的主要指标一致。2.0 s 固定反应窗意味着迟发反应会记为漏答；跨研究比较时应注意，有些 MST 版本采用自定步速或不同延迟，其速度—准确性要求并不等价。

## 参考文献

Azer, L., Vanderlip, C. R., Mayer, L. L., Ehlert, L., Sultzer, D., Shin, H.-W., & Stark, C. E. L. (2026). MST in the wild: Optimizing the mnemonic similarity task for use in diverse environments. *Neuropsychologia, 221*, 109341. https://doi.org/10.1016/j.neuropsychologia.2025.109341

Bakker, A., Krauss, G. L., Albert, M. S., Speck, C. L., Jones, L. R., Stark, C. E., Yassa, M. A., Bassett, S. S., Shelton, A. L., & Gallagher, M. (2012). Reduction of hippocampal hyperactivity improves cognition in amnestic mild cognitive impairment. *Neuron, 74*(3), 467–474. https://doi.org/10.1016/j.neuron.2012.03.023

Jensen, A., Karpov, G., Collin, C. A., & Davidson, P. S. R. (2023). Executive function predicts older adults’ lure discrimination difficulties on the Mnemonic Similarity Task. *The Journals of Gerontology: Series B, 78*(10), 1642–1650. https://doi.org/10.1093/geronb/gbad091

Kirwan, C. B., & Stark, C. E. L. (2007). Overcoming interference: An fMRI investigation of pattern separation in the medial temporal lobe. *Learning & Memory, 14*(9), 625–633. https://doi.org/10.1101/lm.663507

Ma, T., & Zhang, W. (2025). Cognitive modeling of lure discriminability in the Mnemonic Similarity Task. *Behavior Research Methods, 57*(9), Article 253. https://doi.org/10.3758/s13428-025-02785-1

Morcom, A. M. (2015). Resisting false recognition: An ERP study of lure discrimination. *Brain Research, 1624*, 336–348. https://doi.org/10.1016/j.brainres.2015.07.049

Reagh, Z. M., Noche, J. A., Tustison, N. J., Delisle, D., Murray, E. A., & Yassa, M. A. (2018). Functional imbalance of anterolateral entorhinal cortex and hippocampal dentate/CA3 underlies age-related object pattern separation deficits. *Neuron, 97*(5), 1187–1198.e4. https://doi.org/10.1016/j.neuron.2018.01.039

Reagh, Z. M., & Yassa, M. A. (2014). Object and spatial mnemonic interference differentially engage lateral and medial entorhinal cortex in humans. *Proceedings of the National Academy of Sciences of the United States of America, 111*(40), E4264–E4273. https://doi.org/10.1073/pnas.1411250111

Stark, C. E. L., Noche, J. A., Ebersberger, J. R., Mayer, L., & Stark, S. M. (2023). Optimizing the mnemonic similarity task for efficient, widespread use. *Frontiers in Behavioral Neuroscience, 17*, 1080366. https://doi.org/10.3389/fnbeh.2023.1080366

Stark, S. M., Kirwan, C. B., & Stark, C. E. L. (2019). Mnemonic Similarity Task: A tool for assessing hippocampal integrity. *Trends in Cognitive Sciences, 23*(11), 938–951. https://doi.org/10.1016/j.tics.2019.08.003

Stark, S. M., Yassa, M. A., Lacy, J. W., & Stark, C. E. L. (2013). A task to assess behavioral pattern separation (BPS) in humans: Data from healthy aging and mild cognitive impairment. *Neuropsychologia, 51*(12), 2442–2449. https://doi.org/10.1016/j.neuropsychologia.2012.12.014

Vanderlip, C. R., Lee, M. D., & Stark, C. E. L. (2024). Cognitive modeling of the Mnemonic Similarity Task as a digital biomarker for Alzheimer’s disease. *Alzheimer’s & Dementia, 20*(10), 6935–6947. https://doi.org/10.1002/alz.14163

Xie, W., Ma, T., Thakurdesai, S., Kim, I., & Zhang, W. (2025). Discrimination of mnemonic similarity is associated with short-term and long-term memory precision. *Memory & Cognition, 53*(4), 1259–1271. https://doi.org/10.3758/s13421-024-01648-y

Yassa, M. A., Lacy, J. W., Stark, S. M., Albert, M. S., Gallagher, M., & Stark, C. E. L. (2011). Pattern separation deficits associated with increased hippocampal CA3 and dentate gyrus activity in nondemented older adults. *Hippocampus, 21*(9), 968–979. https://doi.org/10.1002/hipo.20808

Yassa, M. A., & Stark, C. E. L. (2011). Pattern separation in the hippocampus. *Trends in Neurosciences, 34*(10), 515–525. https://doi.org/10.1016/j.tins.2011.06.006
