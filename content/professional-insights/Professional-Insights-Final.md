# Professional Insights: Lessons from an EdTech 0-to-1 Journey

Final edited collection

1. Beyond Product Features: Understanding Real-world Adoption
2. The Role Parents Expect Educational Products to Play
3. Beyond AI Capabilities: Defining a Clearer Product Experience
4. From Purchase Appeal to Educational Value


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

# The Role Parents Expect Educational Products to Play

*Understanding learning needs through supervision, independence, and shared participation.*

## Beyond Better Learning Outcomes

While working in an early-stage EdTech company, I encountered parents through user conversations, product activities, and feedback from frontline sales staff. Many wanted products that would support their children’s learning. Yet that shared goal did not mean they expected the same kind of support.

Some wanted help supervising homework. Others hoped a learning device would allow their child to study more independently. Another parent described an ideal product as something she and her child could use to learn and grow together.

These expectations concerned more than educational content. They reflected different ideas about the role a product should play in family life, including which responsibilities it would assume and how parents would participate.

The encounters were informal rather than a representative study. Their value for me lay in revealing distinctions that a broad request such as “help my child learn” could conceal.

## A Companion Toy Expected to Manage Learning

One father’s expectations of an AI companion toy made this particularly clear. He wanted the toy to tutor his child, supervise learning, and provide feedback, while he reviewed progress reports.

His expectation extended well beyond answering questions. It combined several responsibilities: providing explanations, keeping learning on track, and making progress visible to him. He would remain informed while the product handled much of the ongoing activity.

The distinction mattered because conversation, educational content, and reporting could all appear on a feature list without collectively meeting that expectation. A toy might answer questions and summarise interactions while still requiring a parent to initiate practice, redirect attention, or help the child continue.

A progress report could provide visibility into what the product recorded. It would not, by itself, establish that the product had supervised learning effectively.

This helped me identify a more precise product question: which parts of the responsibility the parent wanted to delegate could the system reliably fulfil?

## Supporting the Process of Learning

Other conversations reinforced the distinction between providing resources and supporting their use.

Some parents wanted a family tutor to take responsibility for homework supervision. Explaining difficult material would address one part of that request. Managing homework could also involve getting the child to begin, maintaining attention, responding to resistance, and checking completion.

Similarly, some parents hoped that purchasing a learning device would help their children study independently. Access to content could support that goal, but independence also depended on what happened when a child needed to choose an activity, encountered difficulty, or lost interest.

These observations changed how I interpreted requests for educational support. A team could respond by adding explanations, exercises, or a larger content library while leaving the parent’s main difficulty unresolved. If the difficulty concerned organising daily learning, the product would need to be assessed against that process as well as the resources it offered.

I could not assume that every parent seeking a tutor or device had the same underlying need. The point was to investigate what support meant in each situation before translating it into requirements.

## Shared Learning as a Different Expectation

Another mother described her ideal product as something parents and children could use together to learn and grow.

Her account brought a different form of value into view. The product would help make her participation meaningful, rather than primarily reduce the need for it.

That expectation implied a different experience. A product designed for independent use might offer few opportunities for a parent to contribute. A shared activity would need to give both participants a worthwhile role.

The contrast also made broad labels such as “involved parent” less useful to me. Wanting to delegate homework supervision did not establish that someone wanted less involvement in reading, play, or conversation. Wanting shared learning did not establish that a parent could participate in every session.

I began to understand parental engagement in relation to particular activities and circumstances. A parent might seek help with demanding routines while wanting to preserve enjoyable interactions. This was a possibility to explore, rather than a motive to assign without further discussion.

## Understanding the Work Behind the Request

Requests to delegate educational tasks should not automatically be interpreted as a lack of commitment. They indicate where parents are seeking support; they do not explain, on their own, why that support is needed.

Working hours, caregiving responsibilities, available resources, and the demands of a particular activity could all affect what a family could sustain.

In future user conversations, I would therefore look beyond desired outcomes to how an activity currently happens: who initiates it, where difficulties arise, when an adult intervenes, and which responsibilities the parent wants to retain or hand over.

This would help distinguish requests that initially sound similar. A parent seeking explanations, a parent seeking supervision, and a parent seeking shared learning might all ask for an educational product while expecting substantially different experiences.

## Making the Product’s Role Explicit

The design implication I drew was to make the division of responsibility explicit.

For a learning assistant, I would distinguish answering questions from initiating practice, supporting persistence, checking completion, and informing the parent. Capability in one area should not imply capability across the others.

I would also consider the work the product introduces. Selecting content, configuring goals, interpreting reports, and deciding what to do next can require parental effort. Those activities may be worthwhile, but they belong in any assessment of a promise to reduce supervision.

For shared learning, the focus would differ: what each participant contributes, how they interact, and whether the activity fits the time available. A parent dashboard alone would not create a shared learning experience.

These are implications for future design work, rather than improvements I implemented and evaluated in that role.

The broader lesson was to consider educational outcomes alongside the arrangement through which a family hopes to achieve them. Understanding what a child should learn is essential. Understanding what parents expect the product and themselves to do makes that goal concrete enough to guide product decisions.

---

## Article 3

# Beyond AI Capabilities: Defining a Clearer Product Experience

*How a more specific purpose can guide the design of an AI companion toy.*

## From Capabilities to Purpose

Working with an AI companion toy for children changed how I thought about the relationship between technology and product design.

Conversational AI offered many possibilities: answering questions, telling stories, and responding to a child’s interests. Yet these capabilities did not establish what the toy was primarily for, which interactions it needed to perform reliably, or how it would fit into everyday life.

Describing a product as a companion, tutor, or learning assistant also created different expectations. The same conversational interface could sit behind each description, while the responsibilities implied by those descriptions varied considerably.

I began to see product positioning as a design decision with practical consequences. A clearer purpose could guide which capabilities mattered, how interactions should unfold, and what the complete system needed to support.

## Understanding the Constraints Behind Conversation

Through working with the product and discussing problems with colleagues, I learned that an unsatisfactory conversation could involve microphone input, network connectivity, hardware performance, model selection, response speed, or prompt configuration.

I was not responsible for hardware engineering. Nevertheless, this exposure helped me recognise why a problem that appeared to concern the AI could require attention elsewhere in the system.

It also affected how I thought about expanding the product’s capabilities. A more advanced model might improve some responses, while leaving other sources of friction unresolved. Each additional conversational use case still depended on the supporting system working well enough in its intended setting.

This made the definition of that setting more important. A broad conversational promise left many possible interactions to accommodate. A more specific purpose could help the team identify which interactions deserved priority and what dependable performance would mean.

## Considering Different Forms of Companionship

My observations of other companion products also prompted me to reconsider how much of the experience needed to depend on conversation.

Some products used a recognisable character to give interactions a clearer context. Others placed greater emphasis on physical interaction and expressive behaviour, with less reliance on complex verbal exchanges.

I did not have comparative evidence showing which approach was more effective. These observations were useful as design references: they suggested that character, physical form, and predictable responses could all contribute to a companion experience.

They encouraged me to examine the role of conversation within our product, rather than assuming that broader conversational ability should always be the next development goal.

## Exploring a Habit-Building Assistant

The team later explored positioning the toy as a habit-building assistant for children aged three to six.

The experience combined animated educational content, parental goal-setting, scheduled reminders, NFC cards, and question-based interactions. This provided a more specific context for the product than open-ended conversation alone.

The significance was not simply that the toy had acquired more features. The proposed purpose offered a basis for deciding how those features should work together.

Parental goal-setting could be considered in relation to the routine being supported. Reminders could be assessed in relation to when support was needed. Content and card-triggered interactions could be designed around what the child would encounter at particular moments.

These connections still required design and testing. Their value was that the team now had a more concrete experience to examine, rather than a collection of conversational possibilities.

I left the company before observing the longer-term results. I cannot claim that this direction improved sales, retention, or children’s habits. What I took from it was a change in how the product could be defined and developed.

## Turning a Positioning Decision Into an Interaction

A habit-building purpose would need to influence more than the product description.

It would require decisions about how a routine begins, what prompts the child to act, how the toy responds, and when parental support is needed. It would also require clarity about the contribution of each component.

An NFC card could provide a concrete way to initiate an interaction. A scheduled reminder could establish a recurring prompt. AI-generated responses could offer flexibility within selected exchanges. Each would need to serve the routine rather than merely demonstrate a separate capability.

This helped me understand the relationship between structure and AI. Predictable steps could give the experience continuity, while conversational flexibility could be used where it added value.

The relevant design task would be to decide where each approach belonged. An interaction did not need to be open-ended at every stage to benefit from AI.

## A Clearer Purpose Creates Testable Questions

A more specific use case also makes evaluation more concrete.

For the habit-building direction, I would first examine whether children could understand how to begin, whether the sequence worked reliably, and where adult intervention was required. These observations could reveal problems in the proposed experience before making claims about lasting behavioural change.

The distinction between system activity and user outcomes would remain essential. Delivering a reminder would demonstrate that a prompt was sent, not that a child acted on it. Completing an interaction would not establish that a habit had formed.

A focused product therefore would not automatically be an effective one. It would offer a clearer proposition to investigate, with more specific assumptions that could be examined.

These are considerations I would bring to future product work, rather than an evaluation I conducted in that role.

## Designing Around a Promise the Product Can Support

The companion toy helped me see that progress in an AI product can involve reconsidering its purpose and interaction design alongside improving its technical capabilities.

A broad promise can make many features appear relevant. A specific purpose requires choices: which situations to support, which interactions to prioritise, and what to do when the system cannot respond as expected.

Those choices connect positioning to implementation. Calling a toy a habit-building assistant creates a responsibility to organise the experience around routines and to assess whether that support works. The label alone cannot establish the value.

My main learning was to treat AI as one component of a deliberately designed experience. Its contribution becomes clearer when the product has a defined user, situation, and purpose, supported by interactions the complete system can reliably deliver.

---

## Article 4

# From Purchase Appeal to Educational Value

*Understanding what commercial signals reveal about an EdTech product, and what remains to be examined.*

## Learning to Interpret Commercial Feedback

Working across product operations, user interactions, sales feedback, and marketing activities in an early-stage EdTech company exposed me to different ways of judging a product.

A demonstration could attract attention. A child could express a strong preference. A parent could recognise a potential benefit and consider the price acceptable. These responses mattered to a business trying to establish a market.

They also needed careful interpretation. Interest, purchase, continued use, and educational improvement represented different stages of a product’s relationship with a family. Evidence from one stage could inform decisions without establishing what happened at the others.

This distinction became central to how I understood product value.

## What Makes a Purchase Possible

Through sales conversations and observations of learning devices from established brands, I noticed that purchase decisions could involve several considerations at once.

A child’s enthusiasm could help trigger a purchase. A parent might be willing to buy when the price felt acceptable and the product appeared to offer educational potential.

These observations did not establish how frequently each factor determined a sale. They showed me that a purchase could reflect a combination of immediate appeal, affordability, and expectations about future benefits.

The child’s interest was relevant because the product would need their attention to be used. The parent’s willingness to pay was relevant because it made ownership possible. Neither response established what the child would learn through the experience.

I therefore began to interpret purchase behaviour as evidence about the appeal of a proposition under particular conditions. It was valuable commercial feedback, while leaving questions about everyday use and educational outcomes open.

## The Promise That Enters the Household

An educational purchase carries an expectation about what will happen afterwards.

A learning device might be expected to support independent study. An AI companion toy might be expected to provide explanations, encouragement, or ongoing learning support. The purchase gives a family access to the product; delivering those benefits depends on the experience that follows.

The early AI companion toy made this distinction concrete for me. Its conversational capabilities could invite broad expectations, while the actual experience depended on technical reliability and the limits of the interaction.

A demonstration could show an appealing exchange without establishing how consistently similar exchanges would work in everyday use. Likewise, answering educational questions would not establish that the toy could fulfil the broader role of a tutor.

I did not have evidence to quantify how any gap between expectations and capability affected returns, retention, or satisfaction. The experience nevertheless gave me a reason to examine whether the benefit attracting a family was one the product could dependably support.

This was also where commercial communication and product design met. The way a capability was presented helped define the standard against which the family would judge it.

## Following the Benefit Through Use

Looking back, I would assess a product by following its intended benefit beyond the purchase.

If the proposition centred on independent learning, I would want to understand whether children could begin and continue activities without frequent adult intervention. If it promised learning improvement, I would also need evidence related to the particular knowledge or skill being targeted.

Usage and satisfaction would remain useful, but their interpretation would depend on the claim.

A child returning regularly could indicate interest without revealing what they understood. A parent appreciating reduced supervision could identify a practical benefit without establishing improved learning. Equally, a potentially useful activity would have limited opportunity to help if families rarely used it.

These distinctions would help a team recognise different forms of value. Enjoyment, companionship, convenience, and learning could each matter to users. Identifying which benefit was actually supported would make both evaluation and communication more precise.

For me, this offered a practical discipline: connect each product claim to evidence that addresses it, rather than asking a single favourable metric to demonstrate the product’s overall value.

## Deciding What Needs Attention Next

The working environment also shaped my understanding of the relationship between product quality and commercial execution.

In an early-stage business, improving features, clarifying positioning, setting prices, preparing demonstrations, and reaching customers could all demand attention. A useful product still needed people to discover it and understand its relevance.

At the same time, stronger promotion would not resolve an unreliable core experience. The priority depended on what was limiting the product at that stage.

If users could not reliably obtain the intended benefit, that difficulty required product work. If the experience was sufficiently dependable for its intended use, unclear communication or limited access might become more pressing constraints.

I came to see this as a diagnosis to make with evidence, rather than a fixed sequence in which product development ended and marketing took over. Commercial feedback could expose problems in the proposition, while experience after purchase could reveal whether the underlying promise was being fulfilled.

This was a judgement developed through my work, not a formula I had validated across products.

## Bringing the Proposition and the Evidence Together

In future product work, I would want the benefit highlighted in a demonstration, the experience being built, and the evidence being collected to remain connected.

A tutoring proposition would require attention to the quality of the learning support. A promise of independent use would require attention to adult intervention. Claims of educational improvement would require evidence beyond engagement alone.

These are considerations I draw from the experience, rather than processes I independently implemented or outcomes I measured.

The broader change in my thinking was to follow value across the product’s relationship with a family: what attracted them, what they expected, what they experienced, and what benefit could reasonably be established.

Commercial performance and educational value both mattered. Understanding their relationship required being precise about the evidence available and the conclusions it could support.

