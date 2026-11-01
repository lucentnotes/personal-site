# Professional Insights: Lessons from an EdTech 0-to-1 Journey

Final edited collection

1. Beyond Product Features: Understanding Real-world Adoption
2. Understanding Parents’ Actual Needs: Selective Parental Engagement
3. Beyond AI Capabilities: Designing for the Right Product Experience
4. Commercial Success vs. Educational Value


---

## Article 1
# Beyond Product Features: Understanding Real-world Adoption

*Why a well-designed feature does not necessarily become a meaningful part of users' lives.*

## The Gap Between Product Capability and User Adoption

Working with AI-powered educational products made me realise that technical capability and user adoption are different things. A feature could function as intended while users felt uncomfortable with it, struggled to access its value, or saw little reason to return.

Three experiences helped me examine that gap: a parenting simulation, an AI digital human, and a companion toy for children.

## When a Well-designed Feature Meets Different User Expectations

One example was a scenario-based simulation feature in a parenting mini-program. It allowed parents to practise parent-child communication through simulated conversations with AI.

Parents could take different roles, including viewing a situation from their child's perspective. The system generated responses based on factors such as the child's age, gender, personality, and the specific situation. For example, it could simulate a child misbehaving in a shopping mall. After the interaction, users received a score and a feedback report.

The feature aimed to support reflection through practice. Its feedback acknowledged strengths, identified areas for improvement, and offered suggestions. Yet some parents perceived the experience differently.

Among approximately ten mothers I had direct contact with, around eight expressed some degree of resistance. Their concerns included feeling that the AI was telling them how to be a parent or questioning their parenting abilities. Some also questioned whether the simulated situations accurately reflected the complexity of real family interactions, while others disliked being scored and analysed, feeling that the experience resembled an examination rather than supportive guidance.

These reactions suggested that even a feature designed to provide constructive support could create discomfort when it entered an emotionally sensitive area of users' lives.

### The Difference Between Ideal Behaviour and Actual Behaviour

Another particularly revealing observation came from seeing how the same parent behaved in different contexts.

During actual phone conversations with her child, she could become visibly impatient, focusing heavily on the outcome rather than what the child had experienced along the way. For example, she might insist that she did not care what had happened during the process and only wanted to see the result.

However, when using the AI simulation feature, she presented a noticeably different version of herself. Her responses were much more composed and reflected a more idealised approach to parenting.

In a simulation, users know they are practising and may have more time to consider what they should say. In everyday family situations, however, their responses are also shaped by stress, frustration, time constraints, and emotional reactions.

I could not conclude that users were deliberately misrepresenting themselves. But the observation highlighted an important limitation: **the behaviour demonstrated in a simulated environment may reflect how users believe they should behave, rather than how they actually behave.**

This does not establish that the practice lacked value. It does mean that a composed response in a simulation cannot, by itself, demonstrate improved communication in everyday life.

## Helping Users Explain the Problem

Another challenge emerged when I worked on an AI digital human feature for parents. My responsibilities included designing prompts, defining response boundaries, testing answer quality, and examining unsatisfactory responses.

One recurring issue was that parents would ask for advice without describing enough of the situation. A question such as “My child is fighting. What should I do?” communicated a concern, but left out details that could substantially change the advice: the child’s age, who was involved, what had happened beforehand, and how the parent had already responded.

This was not unique to our product. It reflected a broader challenge in conversational AI: users may know what is troubling them without knowing which information the system needs to offer relevant help. If the AI responds immediately, its advice may remain generic or depend on assumptions that have not been checked.

I considered preparing a usage guide to help parents describe their situations more clearly. Looking back, I still see value in that guidance, but I would also examine how the conversation itself could support them.

A parent seeking help may be frustrated or short of time. Expecting them to read instructions and formulate a detailed request adds effort at the moment they want support. The product could instead ask a small number of relevant follow-up questions before offering advice. The design challenge would be to identify which missing details could materially change the response, while keeping the exchange manageable.

This was a design implication I drew from the experience, rather than an improvement I implemented and evaluated.

The experience changed how I understood usability in conversational products. It involves more than making an interface easy to operate. It also involves helping users express their needs. For an AI parenting product, guiding that process is part of making its capabilities accessible in everyday use.

## The Product Is More Than Its AI Interaction

Working with an AI companion toy for children extended the same question to the complete system. A failed exchange could involve microphone input, connectivity, hardware, model selection, response speed, or prompts.

I was not responsible for hardware engineering, but this exposure helped me understand why improving a model would not resolve every difficulty. From the user's perspective, the product needed to deliver a usable interaction regardless of where a failure originated.

Reliability therefore belonged in the adoption question alongside perceived value and emotional acceptance.

## What This Means for EdTech Product Design

These experiences helped me distinguish functional completeness from value in use. The parenting simulation revealed how feedback could be reasonable yet uncomfortable to receive. The digital human showed why helping users describe a problem could be part of the product experience. The toy made the dependencies behind an apparently simple exchange visible.

They also raised different questions for evaluation. Acceptance would not establish that learning had occurred. A composed simulated response would not demonstrate changed behaviour. A successful demonstration would not establish dependable everyday use.

My work did not establish improvements in retention or learning outcomes. It gave me a more specific basis for examining a product: whether users recognised its value, could access that value, and found the experience relevant enough to use again.

---

## Article 2

# Understanding Parents’ Actual Needs: Selective Parental Engagement

*Why parents may want to remain involved in their children’s growth while outsourcing parts of the educational process.*

## Rethinking Parental Involvement

When designing educational products for families, it is easy to assume that parents either want to be actively involved in their children’s learning or prefer to delegate educational responsibilities to others. However, my experience working with parents in an EdTech company suggested that their expectations were more nuanced.

Some parents wanted products that could reduce the time and effort they spent supervising their children’s learning. Others wanted technology to help them understand their children’s progress without having to manage every learning activity themselves. At the same time, parents could still value shared activities, emotional connection, and opportunities to grow together with their children.

These expectations are not necessarily contradictory. Rather, they suggest that parental involvement is selective. Parents may want to delegate certain responsibilities while retaining the aspects of parenting they find meaningful.

This distinction matters because parental involvement is not simply a matter of willingness. It is also shaped by the time, energy, and resources available to each family. Parents must make choices about where to invest their efforts and which responsibilities they can realistically share with others or delegate to technology.

## What Parents Want to Delegate

One recurring expectation I encountered was the desire to reduce the burden of daily educational supervision.

For example, some parents preferred to have tutors or other forms of support take responsibility for homework supervision. They were not necessarily uninterested in their children’s education. Rather, they wanted to avoid spending a large amount of time managing tasks that could be handled by someone else.

One mother I spoke with expressed this trade-off particularly clearly. She suggested that, given her circumstances, spending more time earning money might be more practical than spending that time helping her child improve academically. This was an individual perspective, not a general attitude shared by all parents. Nevertheless, it highlighted an important consideration: parental involvement competes with other responsibilities, and families may have different priorities depending on their circumstances.

A similar expectation appeared in conversations about AI-powered educational products. A father of a ten-year-old boy, for example, expressed interest in having a robot help supervise his child’s learning, provide feedback, and identify areas for improvement. He imagined being able to review the robot’s reports to understand how his child was progressing, what difficulties he might be experiencing, and what could be done next.

In this scenario, the parent would not need to be physically present throughout the learning process. Instead, technology could take on some routine responsibilities while allowing the parent to remain informed and make decisions when necessary.

Learning devices presented another version of this expectation. Some parents hoped that purchasing a learning machine would encourage their children to study independently, reducing the need for constant parental supervision. However, providing a device does not automatically create independent learning habits. From my observations, children who were not particularly motivated to study might simply ignore the device or use it for purposes other than learning.

This reveals an important distinction: parents may hope to transfer some educational responsibilities to technology, but the product still needs to support the child’s motivation and ability to use it independently.

## What Parents Want to Keep

Although some parents wanted to delegate routine educational tasks, this did not mean they wanted technology to replace their involvement entirely.

In some conversations, parents expressed a preference for products that could help them learn and grow alongside their children. One mother, for example, described an ideal product as something that would allow parents and children to learn together while strengthening their relationship.

This expectation is different from simply asking a product to deliver better academic results. It places value on the experience of learning together.

Interestingly, this does not necessarily conflict with the desire to outsource homework supervision or other demanding responsibilities. A parent may be willing to delegate repetitive or stressful tasks while still wanting to participate in enjoyable activities, conversations, and shared discoveries.

The distinction may lie in the nature of the activity itself. Parents might see homework supervision as a responsibility that requires time, patience, and considerable effort, whereas playing, exploring, or discussing something together can be a more rewarding form of interaction.

From this perspective, the question is not whether parents want to be involved, but what kind of involvement they want to maintain. Technology could reduce the burden of repetitive tasks while leaving more room for encouragement, communication, and shared experiences.

## Designing Around Selective Parental Engagement

These observations suggest that family-oriented educational products should be designed around the different roles and expectations within a family, rather than treating parental involvement as something that can simply be increased or replaced.

First, products should identify which educational responsibilities parents actually want to delegate. Routine practice, progress tracking, reminders, and basic feedback may be suitable areas for technological support. However, these functions should not be assumed to replace every form of parental guidance. A product that generates progress reports, for example, should help parents understand what the information means and what they can do with it, rather than merely adding another monitoring task.

Second, products should preserve opportunities for meaningful parent-child interaction. Rather than attempting to remove parents from the learning process, technology could reduce repetitive tasks and create more room for encouragement, discussion, and shared exploration.

Finally, products need to consider the child’s ability and willingness to participate independently. Parents may hope that technology will reduce their supervision responsibilities, but this outcome depends on whether children find the product understandable, engaging, and useful. A product cannot achieve independent learning simply by transferring activities from parents to children.

Ultimately, parental involvement should not be understood as an all-or-nothing decision. Parents may want to step back from certain responsibilities without stepping away from their children’s development. Their expectations are shaped by the practical demands of family life as well as the emotional value they attach to different forms of interaction.

The challenge for EdTech product design is not simply to replace parental involvement with technology, but to understand how educational responsibilities can be distributed in ways that respect families’ constraints while supporting children’s learning and meaningful family relationships.

---

## Article 3

# Beyond AI Capabilities: Designing for the Right Product Experience

*Why successful AI products need more than advanced technology.*

## The Gap Between AI Expectations and Product Reality

When developing AI-powered products, it is tempting to focus on improving the intelligence of the underlying technology. A more capable model may seem like the most direct way to create a better user experience. However, my experience working with an AI companion toy made me realise that product quality depends on more than the intelligence of the AI itself.

The product was initially positioned as an AI companion for children, with conversational interaction at its centre. However, this broad positioning created expectations that were difficult for the actual product to fulfil. Marketing messages sometimes presented capabilities beyond what the product could reliably deliver. When distributors received the product, some found that the actual experience did not match what they had expected. This contributed to dissatisfaction and the loss of some distributors.

Looking back, the issue was not simply that the AI needed to become smarter. The product's positioning, promised experience, and technical capabilities were not sufficiently aligned.

This experience highlighted an important distinction: an AI product should not be designed around what the technology might theoretically achieve, but around the experience it can consistently deliver in real usage scenarios.

## Rethinking the Interaction Model

An AI companion toy may appear to be a straightforward product: a child speaks to a toy, and the toy responds. Yet delivering this experience reliably involves multiple technical components.

During my work, I became aware of how issues involving hardware heat, microphone quality, Wi-Fi connectivity, model selection, and response speed could all affect the interaction. When a toy failed to respond, the cause was not necessarily the AI model. It could be a problem with sound collection, network connectivity, or another part of the system.

This made me realise that conversational intelligence alone does not determine whether an AI product feels reliable. A conversational product is only as reliable as the system supporting the conversation.

I also observed different approaches to designing AI companion products in the market.

One approach was to build toys around recognisable characters, such as Ultraman. By giving the toy a specific identity, knowledge base, and conversational boundaries, the product could create a more focused interaction. Instead of expecting it to behave like a general-purpose conversational assistant, users would have a clearer idea of what kind of interaction to expect.

Another approach was to limit the complexity of verbal interaction. In the case of Ropet, its CEO insisted that the product should not engage in conversations using complex sentences. This established a clear boundary for the product's verbal interactions. Rather than describing the product simply in terms of limited conversational capability, it is more accurate to recognise that complex, sentence-based conversation was not part of the interaction the CEO wanted the product to offer. Combined with touch responses and pet-like interactions, this approach placed less emphasis on sophisticated conversation and more on creating a simple sense of companionship.

These examples represent different product strategies rather than a universal formula. However, they illustrate an important possibility: when current AI capabilities cannot fulfil every expectation, designers can reconsider the interaction model itself. A product does not always need to simulate human conversation. It may create value through a narrower conversational role, simple responsive interactions, or a combination of physical and digital experiences.

In this sense, defining what an AI product should not do can be just as important as deciding what it should do.

## From General AI Companion to a Specific Educational Purpose

A more concrete example of this thinking emerged when the team reconsidered the positioning of our own toy, named Xiaole.

Rather than continuing to position it broadly as an AI companion, the team shifted towards a more specific purpose: a habit-building assistant for children aged three to six.

This change reflected a closer alignment between the product's actual conversational capabilities and the needs of a more clearly defined age group. At that stage, its conversational abilities were more suitable for younger children than for complex, open-ended conversations. Habit formation also provided a more concrete educational context in which the product could be used.

The team introduced a habit-building package that connected the parent-facing mini-program with the child's interaction with the toy.

Parents could access a growth-goal section in the mini-program. Children first watched short animations created by the team, covering habits and everyday safety topics such as brushing teeth and looking at traffic lights before crossing the road. After an animation, the system generated a corresponding growth goal for the parent to review and confirm.

Parents could then configure reminders, including the time and frequency. When the scheduled time arrived, the toy would remind the child about the target habit.

The experience also included NFC cards. Each card corresponded to an animation topic and contained around ten guiding questions. For example, a card about brushing teeth might include questions about why brushing is important. When a child tapped the card against the NFC area on the toy's body, the toy would randomly select a question and interact with the child. This helped avoid repeating exactly the same question every time.

The different components served distinct purposes. The animations introduced habits in an engaging format, the parent-facing mini-program allowed adults to set and manage goals, and the NFC cards gave children a way to initiate interactions independently, even when their parents were not present.

The product therefore involved three connected roles. Parents selected and managed growth goals, children engaged with the content and initiated activities, and the toy provided reminders and guided interactions around specific habits.

Rather than relying entirely on open-ended AI conversation, the product used a more structured interaction model. Its educational purpose was clearer, and the activities were connected to specific everyday behaviours.

This repositioning represented an attempt to move from a broad promise of AI companionship towards a more defined educational use case. It also changed how the product experience was organised: instead of expecting the toy to serve as an unrestricted conversational companion, the team designed a more structured experience around habit formation.

However, a clearer positioning did not automatically guarantee commercial success. From my impression at the time, the product did not achieve particularly strong sales. Since I had left the company, I could not observe its longer-term performance or determine the reasons behind this outcome. Earlier distributor dissatisfaction, product experience, and other market or channel factors may all have played a role, but I cannot establish a direct causal relationship.

The important point is that repositioning a product is only a starting point. The revised experience still needs to be validated through actual use and market feedback.

## Designing Around the Experience, Not Just the Technology

These experiences changed how I think about AI product design.

First, product positioning should reflect what the technology can reliably deliver. Broad claims about AI companionship or intelligence may create expectations that are difficult to meet. A more specific use case can help users understand the product's purpose and what they can reasonably expect from it.

Second, the interaction model should be designed around the target users and context. Complex conversation is only one possible form of interaction. For younger children, structured prompts, physical interactions, reminders, and simple responses may be more appropriate than unrestricted conversation.

Third, the entire system needs to support the promised experience. Hardware, connectivity, interaction design, and AI capabilities are interdependent. Improving one component cannot necessarily compensate for weaknesses in another.

Ultimately, the goal should not be to make every AI product as intelligent as possible. It should be to identify an experience that is valuable to its intended users and can be delivered consistently with the available technology.

A well-designed AI product is not necessarily the one with the most advanced AI. It is the one that makes the best use of its capabilities to deliver a clear, reliable, and meaningful experience.

---

## Article 4

# Commercial Success vs. Educational Value

*Why a product that sells well is not necessarily a product that delivers meaningful educational outcomes.*

## When Commercial Success Is Mistaken for Educational Value

In the EdTech industry, commercial success can easily be mistaken for evidence of product quality. A product that sells well may appear to have successfully addressed users' needs. However, my experience gradually made me realise that commercial performance and educational value are not the same thing.

For example, some learning devices from well-established brands achieve strong sales. Their market performance may indicate that parents recognise their appeal or consider them worth purchasing. However, sales figures alone cannot tell us whether children have learned more effectively through using them.

An educational product can be commercially attractive because of its brand, features, presentation, convenience, or perceived educational benefits. These factors may influence purchasing decisions, but they do not necessarily demonstrate the product's actual contribution to learning.

This distinction is particularly important in EdTech because the person who pays for a product is often different from the person who uses it. Parents may make the purchasing decision, while children are the primary users. What motivates a parent to buy a product may therefore differ from what makes it useful or effective for a child.

## What Makes Parents Decide to Buy?

During my experience in the industry, I noticed that a child's preference could sometimes be a powerful trigger for a parent's purchasing decision.

For instance, when a child strongly wants a particular product, parents may be willing to buy it as long as the price falls within their acceptable range. In this situation, the purchase may be driven more by the child's enthusiasm and the parent's willingness to fulfil that preference than by a detailed evaluation of the product's educational effectiveness.

This does not mean that parents do not care about education. Rather, purchasing decisions are influenced by multiple considerations, and educational value is not necessarily the only deciding factor.

It also means that purchase intention and educational expectations should be understood separately. A child may want a product because it looks attractive or offers enjoyable interactions. A parent may agree to buy it because the price is acceptable and the product appears worthwhile. Neither decision, by itself, establishes whether the product supports meaningful learning.

This made me question whether purchase intention should be treated as evidence of educational value. A successful transaction tells us that someone was willing to pay for the product. It does not tell us what the child gained from using it.

## Product Quality Sets the Foundation, but Does Not Explain Everything

Another important lesson came from observing the relationship between product development and commercial execution.

In the early stages of bringing a product to market, product quality matters enormously. A product needs to meet an acceptable standard and deliver on its core promises before sales teams and distributors can confidently promote it.

I saw this in the case of our AI companion toy. When the actual product experience did not match the expectations created by its market positioning, some distributors were dissatisfied and stopped working with the product. This illustrated how a gap between product promises and actual delivery can undermine commercial confidence.

However, once a product reaches an acceptable level of quality and can reliably fulfil its main purpose, the factors influencing further growth may change. Sales, marketing, distribution channels, and operational execution can become increasingly important.

In other words, product quality establishes the foundation for market entry, while go-to-market execution can become more important for expanding market reach once the product meets the market's minimum expectations.

This does not mean that product quality becomes irrelevant after launch. Rather, the relative importance of different factors may shift depending on the product category and its stage of development.

For example, products such as computers are often evaluated heavily in terms of performance and technical specifications. Users may have clear expectations about processing power, reliability, and other functional capabilities. In such categories, product performance itself can remain a major competitive factor.

An AI companion toy, on the other hand, may not need to demonstrate the most advanced AI capabilities available. What matters more may be whether it delivers a satisfactory experience in its intended use case. If it can fulfil that core purpose reliably, its commercial performance may depend increasingly on how effectively it is positioned, marketed, and distributed.

The key is not that one factor is always more important than another. It is that the factors supporting commercial success vary across products and stages.

## Commercial Performance and Educational Outcomes Are Different Measures

These observations led me to distinguish several dimensions that are often treated as if they were interchangeable.

Commercial attractiveness: Whether the product appeals to potential buyers and creates a willingness to purchase.

Perceived educational value: Whether parents believe the product can contribute to their children's learning or development.

Actual learning effectiveness: Whether using the product leads to meaningful improvements in children's knowledge, skills, or learning behaviours.

User satisfaction: Whether parents and children feel that the product meets their expectations and provides a worthwhile experience.

Continued usage: Whether users continue to engage with the product after the initial purchase.

## Evaluating an EdTech Product Beyond Sales

My experience has made me more cautious about treating market success as a direct indicator of educational quality.

Commercial success matters because an educational product needs to reach users and remain viable. However, commercial viability and educational effectiveness answer different questions. One concerns whether a product can attract buyers and sustain a business; the other concerns whether it genuinely supports learning.

For product teams, this distinction matters because designing for purchase is not the same as designing for learning. A product may need to appeal to parents, engage children, fulfil its educational purpose, and remain commercially sustainable. These requirements overlap, but they cannot simply be reduced to one measure of success.

Ultimately, an EdTech product should be evaluated from both commercial and educational perspectives. Sales can tell us whether a product has found a market. Actual usage and evidence of learning are needed to understand whether it has fulfilled its educational purpose.

Commercial success can demonstrate that a product has found a market. It does not, by itself, demonstrate that the product has fulfilled its educational purpose.

