![GitHub Workflow Status](https://img.shields.io/github/workflow/status/thisaintwork/AgileDungeonTrekking/Django%20CI?style=plastic)

# AgileDungeonTrekking
This is the repository for Fall CSCI-E71 for the Traveling Players project

The project is tracked in the "AgileDungeonTrekking" repo: https://github.com/thisaintwork/AgileDungeonTrekking

We used Miro for weekly scrum meetings. The first board was used for weekly scrum initally: https://miro.com/app/board/uXjVPK-7qnU=/
We moved to this board: https://miro.com/app/board/uXjVPINzDBE=/. It's a simplified version that focuses on what's working well and isn't working well at the team and project level, rather than by individual and is better suited to the needs of our team. 

We also keep a homework backlog in our Github repo here: https://github.com/orgs/thisaintwork/projects/3/views/1

**Team Name**: Traveling Players

**Team Members:**
Kelly Robertson - Product Owner
Drew Fitzgerald - Developer
Mike Reekie - Developer
Diana Liu - Scrum Master

**Roles & Responsibilities**

The Product Owner is also accountable for effective Product Backlog management, which includes:
- Developing and explicitly communicating the Product Goal;
- Creating and clearly communicating Product Backlog items;
- Ordering Product Backlog items; and,
- Ensuring that the Product Backlog is transparent, visible and understood.

The Scrum Master serves the Scrum Team in several ways, including:
- Coaching the team members in self-management and cross-functionality;
- Helping the Scrum Team focus on creating high-value Increments that meet the Definition of Done;
- Causing the removal of impediments to the Scrum Team’s progress; and,
- Ensuring that all Scrum events take place and are positive, productive, and kept within the timebox.

The Developers are the people in the Scrum Team that are committed to creating any aspect of a usable increment each Sprint. The specific skills needed by the Developers are often broad and will vary with the domain of work:
However, the Developers are always accountable for:
- Creating a plan for the Sprint, the Sprint Backlog;
- Instilling quality by adhering to a Definition of Done;
- Adapting their plan each day toward the Sprint Goal; and,
- Holding each other accountable as professionals.

Only the developers pull stories into the sprint backlog.

=======
**Canvas Group Name**: Group 4

**Discord Channel**: https://discord.com/channels/1008812300305702912/1035178215834128395

**Product Name**:  Agile Dungeon Trekking

**Product Description**:  Open source app that allows a Dungeon Master and a group of D&D players to store information about their campaign including character details, maps, non-player character (NPC) details, group loot, session notes, and personal notes. 

**Far Vision**:  Simplify gamepay and bring D&D into the digital age for a new generation of gamers.
=======
**Far Vision**:  Play better together even when you are far away - Improve gameplay and collaboration for teams playing in person or online across multiple campaigns and player characters

**Near Vision**: Play better together - Improve game play for team members playing as a single team running a campaign

**Stakeholder Types:**
- Dungeon Master
- Player in a team/campaign
- Player looking for a team/campaign
- Experienced player (> 1 yr playing)
- Inexperienced or beginner player ( < 1 yr playing) 

**User Persona:**
- Name: Lexi Player One (real person)
- Role: Player in a team campaign - Druid
- Age: 12
- Gender: F
- Computer Skills: Word, Excel, Powerpoint, Google suite, internet browsers
- Apps Used: TikTok, Instagram, You Tube
- D&D Skills: first campaign
- Motivation: have fun, role play 
- Desires/wants/needs: Change into animals, make friends with NPC animals

**Initial Product Backlog**:
- Located here: https://github.com/orgs/thisaintwork/projects/3/views/2
1. Shape change options 
2. Animal stats 
3. Take notes 
4. Share notes 
5. Information about NPCs
6. Match NPCs to Quests
7. Track party loot and gold
8. Quest names & steps
9. Track progress against quests
10. Track party movement
11. Special party rules

**Rationale for Backlog Ordering**:
As the product owner, I ordered the baseline based on our interview with Lexi Player One. I took this approach so that we could get an early win with one of our stakeholders. 

**True User Stories for PBIs**
**1. Title:** Shape change options 
- **Opening & Details:** As a druid and I want to know which animals can I shape change into because the options change based on my level and character. There are size classes for the animals in D&D and I can only change into the animals that are a certain size. I also have to have seen the animal before either "in person" or through some kind of magic effect. Bascially I need to matching my level to the set of animals in the right size class that I have seen. We use the D&D 5e rules.
- **Acceptance Criteria:** A website exists. The DMs and players can log into the website. The website had a section for animals. Animals have an image and descriptive text. Players can select and animal to see it's stats. Players can find and choose the right animal for a game scenario in 5 min. 

**2. Title:** Animal stats 

- **Opening & Details:** As a druid, once I have a set of animals to choose from, I want to know things like health, attacks (magic and melee), resistences, proficiencies etc because I need some idea of what I can do when I change into that animal. When I change into an animal, it replaces my druid character. I can change back to my druid at any time, then I will go back to the same character configuration I was at when I initiated the shape change. For example, if I had 35 of 48 health points available as a druid, when I shaped change I gain the full health points of the animal. When I change back to a druid, I return to 35 of 48 health points. 

=======
- **Opening & Details:** As a druid, once I have a set of animals to choose from, I want to know things like health, attacks (magic and melee), resistences, proficiencies etc because I need some idea of what I can do when I change into that animal. When I change into an animal, it replaces my druid character. I can change back to my druid at any time, then I will go back to the same character configuration I was at when I initiated the shape change. For example, if I had 35 of 48 health points available as a druid, when I shaped change I gain the full health points of the animal. When I change back to a druid, I return to 35 of 48 health points. Here is an example description of an animal:
- ![image](https://user-images.githubusercontent.com/113219148/198417449-67603b92-ee90-4d8b-997d-5522c0e87071.png)

- **Acceptance Criteria:** A website exists. The DMs and players can log into the website. The website had a section for animals. Players can select an animal into which to shape change. The app will ask players to confirm their selection. When a player confirms their selection for shape change, the app replaces the player's character sheet with the animal's character sheet with armor class, hit points, speed, stats (strength, dexterity, constitution, intelligence, wisdom, & charisma), skills, attributes, and actions. When a player leaves animal form, they revert back to their original character sheet as it was at the time of their shape change. 

**3. Title:** Take notes 
- **Opening & Details:** As an inexperienced player, I want to take notes during the game so that I can remember the important things that happened during our session. Usually I write down enough notes to fill one side of an 8" x 11" piece of ruled paper. Instead, I would like to enter notes as I am playing.
-  **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for notes that will store at least 18,000 characters (including spaces) for each session played up to 1000 sessions. The note can be edited in real time. The notes can be accessed between game sessions.

**4. Title:** Share Notes 
- **Opening & Details:** As an inexperienced player, I want to share notes with my team so that we can share information. I don't want to change my friend's notes by mistake, but I want to be able to add comments.  
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for notes that will store at least 18,000 characters (including spaces) for each session played up to 1000 sessions. Players can see notes written by their team mates.  Notes are tagged with the author's name and a date-time stamp recording the last time the notes were edited. Players can add comments to other's notes. Comments are tagged with the tagged with the author's name and a date-time stamp recording the time of submission. A players can not change another player's notes.  

**5. Title:** Information about NPCs
- **Opening & Details:** As a player, I want to track which NPCs we meet and why they are important so I can use the information in future sessions. It would be nice if I could find the proper spelling of the NPCs name and an image of them as well, because that will help me remember. I only need to enter a few sentences for each NPC, but I may want to add more information over time. 
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. Website has a section for NPC information that can store at least 1000 NPCs with at least 5 MB of image data and 18,000 character of text for each NPC (including spaces). DM and the players can add text and upload one image file to the NPC section. Uploaded images are displayed above associated text. DM and players can edit their own notes at any time. DMs and players can not change other's notes. 

**6. Title:** Match NPCs to Quests 
- **Opening & Details:** As a player, I want to track which NPCs gave me quests, so that I know where to bring the quest items and information once they are aquired. My group usually works on multiple texts at a time, so we can get confused. It would be nice to be able to tag quest items with the quest name, delivery location, and recieving NPC/entity. Sometimes we carry quest items for multiple sessions and I don't want to sell them by mistake. 
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for quests. The website has a section for NPCs. The website allows players to link each NPC to one or more quests. Each NPC is associated with one or more locations, quests, and/or quest items.

**7. Title: Track party loot and gold**
- **Opening & Details:** As a party, someone needs to keep track of party loot and gold, so we can efficiently share items and buy goods. Sometimes my party will swap gear before an encounter so we have the right armor, weapons, and spell items for the next challenge.
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for party loot that will store a table up to 5,000 rows and 100 columns where each cell can hold at least 500 characters of text.

**8. Title:** Quest names & steps 
- **Opening & Details:** As a party, all players must know quests names and steps so that we have a common understanding of the game status. I like to take notes on quests each time we complete a step or get information related to the quest. 
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for quests that will store at least 3,600 characters (including spaces) for each quest up to 500 quests . Each quest has a name, and is tagged with a start location, end location, and associated NPC/entity for delivery. The website allows players to link each quest to one or more NPCs. 

**9. Title:** Track progress against quests 
- **Opening & Details:** Sometimes our party forgets which steps we still have to accomplish to get a quest done. I'd like to check off quest steps when we complete them, and also know what quests we have already done.
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website had a section for quests taht will store. The DM and the players can enter quest names. Players can enter quest steps. Players can mark steps complete. Once all of the quest steps are complete, the quest name is automatically marked complete. The DM can delete quest names and steps. The players can delete quest steps, but not quest names. 

**10. Title:** Track party movement 
- **Opening & Details:** As a player, I need to know where I am in the D&D world. Usually, we have to travel to different locations to accomplish quest items. If we know where we are on the “world” map, then we can plan the best route and order of our quest steps much easier. Sometimes we split the party and go to different locations and need to plan where we will meet up again.
- **Acceptance Criteria:** A website exsists.  The DMs and players can log into the website. The website has a section for maps. DM can load map files onto the website. DM can place player tokens on one or more maps. Players can see the maps that the DM has loaded on the website. Players can see all tokens that the DM has placed on the maps. Players can not move tokens. 

**11. Title:** Special party rules 
- **Opening & Details:** As a player, I want to have a website where I can find the special party rules that the DM created for my campaign. I sometimes forget these rules and they are not in any books or on the internet because they are only being used by our team. I need to know the rules so I can take advantage of them.
- **Acceptance Criteria:** A website exists. The DMs and players can log into the website. The website has a section for party rules. The DM can enter and save the special party rules. The DM can edit and resave the rules as many times as they want. Players can read the special party rules.

**Definition of Ready**:
- User story has a title
- User story opening sentence
- User story additional details
- User story has a clear, complete acceptance criteria
- User story is estimated in story points
- User story addresses a business need
- User story has measurable acceptance criteria
- User story is small enough for implementation in the given time, but large enough to provide customer value
- Infrastructure and development tools are ready
- User story meets the INVEST (Independent, Negotiable, Valuable, Estimable, Small & Testable) criteria


**Estimating**
- PBIs have been estimated in Github using story points. Story points can be found in each PBI on the right-hand side under “show all fields”.
- Our team conducted an “affinity estimating” activity. The results of this activity can be found in Github under the Affinity Estimating tab here: https://github.com/orgs/thisaintwork/projects/3/views/4.
- As a side note: Only developers participated in estimating PBIs.


# Project Part 2: First Sprint

## Sprint Planning:

**1.) Forecast for story points per sprint:** 12

**2.) Rationale for forecast:** Developers needed to produce working software. They found that 12 user story points would be the minimum number necessary to achieve this. Given individual skills and time constraints, 12 seemed like a reasonable forecast for a first sprint.

**3.) Note:** Only developers participated in moving items from product backlog into sprint backlog

**4.) Some of the stories in the sprint backlog were greater than half of the forecast velocity for the sprint. These stories were split into smaller stories with new estimates.**

**5.) User stories were decomposed into developer tasks. These tasks are listed within each sprint backlog item. The aggregate size of the stories does not exceed our forecast.**

**6.) Sprint Backlog, kanban board URL:** https://github.com/orgs/thisaintwork/projects/3/views/2

**7.) Sprint Burndown Chart, URL:**
https://miro.com/app/board/uXjVPINglNY=/
![image](https://user-images.githubusercontent.com/54752285/201235948-837bcb2d-b030-49bf-8e62-adaf6dbd6147.png)

## Daily Scrums 

**Daily Scrum held on:** : Two of these are documented directly in this readme, but we maintain record of the meetings in Miro here: https://miro.com/app/board/uXjVPINglNY=/

- 3 November 2022,  6 pm- 7 pm

- 7 November 2022,  5 pm- 6 pm

- 8 November 2022,  6 pm- 7 pm

- 9 November 2022,  6 pm- 7 pm

- 10 November 2022, 6 pm- 7pm (Sprint Restrospective/Sprint Review)



**8.) Documentation for daily scrum on:** 3 November 2022, 6 pm- 7 pm
- **9.) includes Last 24 for each team member**
- **10.) includes Next 24 for each team member**
- **11.) includes impediments and impediment removal plans for each team member**


![image](https://user-images.githubusercontent.com/54752285/200216858-2aacc1c1-4809-4faf-a600-d8ceb009a470.png)

Collected notes from daily scrum discussion on 3 November 2022-

Kelly: 
- Last 24: Reviewed Part 2 Assignment 
- Next 24: Start Backlog
- Impediments: Hungry
- Impediment removal plan:Eat

Diana: 
- Last 24: Contacted the Professor about Miro, Built Miro board for team scrum, planned meeting agenda, scheduled team meetings, shared a Colab notebook with team for dev
- Next 24: Schedule team meetings for remainder of term, update and manage Miro board, document Scrum in Readme, begin research for programming, share dev research with others
- Impediments: Tired
- Impediment removal plan: Rest at end of sprint, 

Mike: 
- Last 24: Dev meeting, added dev items into backlog, broke down backlog items
- Next 24: Look at Colab, work on dev setup, work on backlog items, put homework items into GIT, snapshot of Miro, look at examples of projects
- Impediments: None identified
- Impediment removal plan: None identified

Drew: 
- Last 24: Brain storm with Mike and flowchart
- Next 24: Backlog
- Impediments: Not having a sprint backlog
- Impediment removal plan: Create a backlog and agree to it Monday, begin some research for programming over the weekend

Collected Notes from 9 November Daily Scrum
![image](https://user-images.githubusercontent.com/54752285/201750574-14dff8ba-8ada-43e7-b2a4-ad61548bd581.png)

Kelly: 
- Last 24: Broke out user stories
- Next 24: Added user stories
- Impediments: Next steps
- Impediment removal plan:Discuss a plan for next steps

Diana: 
- Last 24: Built Django landing page in Pycharm, page includes password and login, commit code to Git, plan agenda, update scrum board, work on burndown chart, update Miro, document source code for Django landing page/environement and share with team 
- Next 24: Unit test research, unit testing, resources for subpages
- Impediments: Tired
- Impediment removal plan: Rest at end of sprint

Mike: 
- Last 24: Put technical tasks in kanban into Miro, make stories smaller
- Next 24: Review sprint stories, Digital Ocean signup, PBI sizes in title
- Impediments: Blocked on how to set up dev environment
- Impediment removal plan: Diana shares documentation for setup of environment and helped with questions

Drew: 
- Last 24: Researched Django and webhosting, broke down some of the stories, and changed the scheme in the backlog
- Next 24: Unit test setup, PBI estimates
- Impediments: Could not set up Digital Ocean since lacked needed GIT access
- Impediment removal plan: Mike has needed GIT access and will work on Digital Ocean

**12.) Evidence of updating sprint task board and burndown chart, URL:**
![image](https://user-images.githubusercontent.com/54752285/201235948-837bcb2d-b030-49bf-8e62-adaf6dbd6147.png)
https://miro.com/app/board/uXjVPINglNY=/

**13.) Evidence of pair/mob programming, URL:** [Mob Programming image](https://github.com/thisaintwork/AgileDungeonTrekking/blob/main/sprint1_mob_programming.JPG)

**14.) Evidence of unit tests, URL:** 
- [unit test file] (https://github.com/thisaintwork/AgileDungeonTrekking/blob/main/account/tests.py)
- [passing tests screenshot] (https://github.com/thisaintwork/AgileDungeonTrekking/blob/main/sprint1_testing.JPG)

We keep a Word file (Agile Dungeon Trekking TDD.docx) that documents our Test-first (TDD) approach-including 11 unit tests-within the Kanban for PBI #89 at https://github.com/thisaintwork/AgileDungeonTrekking/issues/89.




## Sprint Review
**15.) Sprint review held on:** November 10, 2022 6-6:30 p.m.

**16.) Working software, URL:** [Agile Dungeon Trekking](http://agiledungeontrekking.online). At this time, we have further development to complete in Digital Ocean to sync up completely between GIT and our public space. However, we welcome you to visit our login page at the URL above. We also invite you to view the pages as captured below by locally running the code hosted here in GIT: ![image](https://user-images.githubusercontent.com/54752285/201746844-d711ba5c-da31-478d-9802-c33ef464fa26.png)
The image for the landing page was built by Dall-e
![image](https://user-images.githubusercontent.com/54752285/201747163-b5d2179c-3949-4fe0-b677-deea1312d80c.png)

This page is the beginning of development for a subpage:![image](https://user-images.githubusercontent.com/54752285/201747238-2fc2ff9e-6d31-459c-91f1-89df4fd061e7.png)

	 




**17.) Evidence of stakeholder attending Sprint Review:** [Sprint1 review](https://github.com/thisaintwork/AgileDungeonTrekking/blob/main/Sprint%20Review_0.png)

**Feedback**: We demoed the product to our stakeholder and received the following feedback:
- update user interface so text is easier to read.
- allow user to upload images.

(Note: product backlog was revised based on feedback received.) 

For Sprint Review feedback, See item: [Issue #90](https://github.com/thisaintwork/AgileDungeonTrekking/issues/90)

## Sprint Retrospective
**18.) Sprint review held on:** November 10, 2022 6:30-7 p.m.

Team Retrospective | Date: 10/31/22- Close out on PI and Start S1

LIKED
What was good? We all came together as a team   One of us, in this case Drew did a review of what we did.   Diana started taking on the role of leading meetings and rounding us up   We did a really good job. This was our first sprint.   We figured out a way to coordinate who worked on what items   The checkins were helpful for Diana (and everyone else) for knowing how we can help each other and what we need to add to the agenda.  	

LEARNED
What did the team learn? 
 How we work well   We should break down the stories sooner and as a team.   we are learning that we can ask each other for help on things that each brings to the table  

LACKED
What did the team lack?  Time. With our outside lives and jobs it never felt like we had enough time   Lacked experience with the tools that we are using. (Have since learned at least the basics)   We were learning as we went. There are things that I would have liked to have done better.  It will get better but we did not understand some of the tools and the agile techniques  when we started this sprint  	

LONGED FOR
What did the team long for? Better understanding of BDD   for Mike to talk less  


- **action to improve team:** Our team discussed several issues in the Sprint Retrospective. One issue that was discussed is Test-Driven Development. In order to address this issue our team identified the action: “conduct testing earlier and more frequently.” This action was added to our product backlog with acceptance criteria. It is at the top of the backlog and will be pulled into the next sprint.

For Sprint Retrospective action, see item: [Issue #91](https://github.com/thisaintwork/AgileDungeonTrekking/issues/91)
![image](https://user-images.githubusercontent.com/54752285/201748970-2792b17f-558b-42e2-96c5-9004c64d385c.png)

**19.) Note: All of the PBIs in backlog are true user stories**




# Project Part 3: Second Sprint

**1.) Forecast for story points per sprint:** 12

**2.) Rationale for forecast:** Yesterday's weather.

**3.) Note:** Only developers participated in moving items from product backlog into sprint backlog

**4.) Some of the stories in the sprint backlog were greater than half of the forecast velocity for the sprint. These stories were split into smaller stories with new estimates.**

**5.) User stories were decomposed into developer tasks. These tasks are listed within each sprint backlog item. The aggregate size of the stories does not exceed our forecast.**

**6.) Sprint Backlog, kanban board URL:** https://github.com/orgs/thisaintwork/projects/3/views/2

**7.) Sprint Burndown Chart, URL:**![image](https://user-images.githubusercontent.com/54752285/204190988-104465af-80c8-44e2-b50a-41f0e800006e.png)
We used Miro and continued to track our burndown chart in the chart used in the first sprint: https://miro.com/app/board/uXjVPINglNY=/

## Daily Scrums 

**Daily Scrum held on:** : 15, 16, 17, 23, and 25 Nov. from 6-7:00 pm; Typically, these meetings ran until 7:30 or 8 to allow more time for technical discussion as well. 

Two of these are documented directly in this readme, but we maintain record of the meetings in Miro here: https://miro.com/app/board/uXjVPINglNY=/

**8.) Documentation for daily scrum on:** 
- **9.) includes Last 24 for each team member**
- **10.) includes Next 24 for each team member**
- **11.) includes impediments and impediment removal plans for each team member**



Notes from team scrum on 15 Nov broken down by person:
Diana   

Last 24: Miro, met with professor about Miro, write unit tests, TDD, document TDD and share with team, agenda for meeting/share agenda, research subpages   

Next 24: Miro, research character/beast dev, message Mike with idea on Digital Ocean issue   

Blockers:    


Mike-filled this in based on discussions in the meeting, Mike joined toward the end due to another obligation. 
Last 24:  Working on an issue in Digital Ocean; put homework in backlog
Next 24: Fix issue in digital ocean; 
Blockers: Unable to attend, but team would relay information to Mike via Git, Discord, and phone conversation, as well as when he rejoined the next week's scrums

Drew
Last 24: researched Django, 
Next 24: velocity decided, estimate PBIs
Blockers:

Kelly
Last 24: Started HW3 backlog
Next 24: Finish HW3 backlog, Product backlog grooming
Blockers:
![image](https://user-images.githubusercontent.com/54752285/202337028-d476ab4c-3906-4760-9adb-1dbe86d17304.png)



Notes from team scrum on 25 Nov broken down by person:

Diana
Last 24: TDD, wrote unit tests, move files to Git, switched from SQL to postgres, shared documentation on postgres with team, created character TDD and shared documentation with Team, MIRO board, agenda, plan dev timeline
Next 24: Miro, research character dev, build CI/CD pipeline, document CI/CD pipeline, finish building tests, get API running in Digital Ocean, update the team readme, update the kanban as needed
Blockers: 

Mike-
Last 24: moving DNS to Heroku, asked Prof about testing, looked into deployment/testing briefly
Next 24: Postgres; Digital Ocean
Blockers: SSL certs, stake holder could not make it to the meeting, build failing in digital ocean

Drew
Last 24: CI/CD review
Next 24: Digital Ocean
Blockers:

Kelly-unable to attend this meeting due to unexpected event
Last 24: CI/CD review /n
Next 24: Communicate with Diana and Team for Product Review -Virtually, upload jpg of Mind Map to GitHub /n
Blockers:Unexpected schedule conflict, team adapted and Mike subsituted for Kelly; Diana corresponded with documentation (see link below) for email correspondence feedback from stakeholder and product owner

![image](https://user-images.githubusercontent.com/54752285/204192328-bd90465a-31e0-49f7-87d4-ee3a03196d18.png)

Impediments: A couple team members had schedule conflicts with our ususal meeting times and one was unable to attend meetings during the course of the week. When possible, we adapted our schedule to meet at the best time for the team, and considered time and effort availability in sprint planning. Team members helped in ways that were outside of the scope of their traditional roles to accomodate for any gaps in the workflows.

**12.) Evidence of updating sprint task board and burndown chart, URL:**
https://miro.com/app/board/uXjVPINglNY=/
![image](https://user-images.githubusercontent.com/54752285/204195355-1b39759d-5a5a-437a-a865-a61129133ef9.png)
Also, see images above for Sprint Daily.

**13.) Evidence of pair/mob programming, URL:** 


**14.) Evidence of unit tests, URL:** 
- [unit test file] (https://github.com/thisaintwork/AgileDungeonTrekking/blob/main/account/tests.py)
- [passing tests screenshot]

We keep a Word file (Agile Dungeon Trekking TDD.docx) that documents our Test-first (TDD) approach at https://github.com/thisaintwork/AgileDungeonTrekking/issues/89.



## Sprint Review
**15.) Sprint review held on: November 25, 2022 6-6:30 p.m.

**16.) Working software, URL:** [Agile Dungeon Trekking](http://agiledungeontrekking.online)



## Sprint Review
17.) Sprint review held on: November 25, 2022 6-6:30 p.m.
Our Product Owner and Stakeholder planned to attend but unexpectedly were not able. 
Team members present voted to enable Mike to temporarily perform the role of Product Owner while we continued the review.
We also shared documentation of progress (https://docs.google.com/document/d/1VcrI3M1l4KAXeir3y_HONhRB29AsJDPBYRuy2akJA3M/edit) and communicated outside of the planned meeting via email. Our Product Owner/Stakeholder gave this feedback:
![image](https://user-images.githubusercontent.com/54752285/204181276-ab218706-4eb3-45f9-98b6-6fd0bb31595c.png)
This echoes Mike's feedback. At the time of the meeting, the website was working locally but not yet on our publicly hosted site. 

Takeaway: In a future sprint, we'd like to push develepment into production sooner, so it is viewable by our product owner at the time of review. We've added this into the backlog for next sprint (PBI #108).

## CI/CD
**18.) Evidence of Continuous Integration:

**19.) Evidence of Continous Delivery:


## Sprint Retrospective
**18.) Sprint retrospective held on:** 

Team Retrospective | Date: 

LIKED: Getting into a groove, meetings were smooth, understanding eachother better

LEARNED: Team timing, adaptability, tools


LACKED: Time to make things better, digital ocean experience


LONGED FOR: More time

![image](https://user-images.githubusercontent.com/54752285/204195960-d6a2725f-4b0d-4c06-8315-47a23fccbcab.png)
Also viewable via Miro here: https://miro.com/app/board/uXjVPINglNY=/

- **action to improve team:**

For Sprint Retrospective action, see item: #108 in backlog; Our team agreed that while we had working code locally, it was not working live at the time of our review. We agreed we would like to start moving code into production sooner. 

**19.) Note: All of the PBIs in backlog are true user stories**
 






