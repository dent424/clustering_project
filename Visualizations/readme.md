Readme File for Alex Moore's Data Visualization Project

Summary
Since 1972, the University of Chicago has run the General Social Survey (GSS) monitoring social attitudes in the United States. In 2010, the GSS included multiple questions on Americans' perceptions regarding environmental issues. While there are significant variations in the data, it is clear that there is a robust interest in protecting the environment in the US tempered by a reluctance to engage in many concrete activities.

Initial Design Decisions

-Data Design:
Since the survey was presented to survey respondents in a multiple choice format with multiple questions, I chose to aggregate the data into a series of counts for the presentation. For example, there were often questions presented with 5 point Likert scale answer choices ranges from "Strongly Disagree" to "Strongly Agree." I this case I would count up the answers for each answer choice. 

The data also often included a choice for "Don't Know" or "Can't Answer." In the data cleaning phase these items were removed. Since this would result in a different count, making it hard to compare between questions, I decided to convert the counts into percentages of people who answered the question. This allows for easier comparisons between charts.

-Chart Type:
My initial notion was to use stacked bar charts to communicate the entirety of the dataset in a single interactive chart. This proved to be untenable because the text of the questions was long. This would mean that the question text would need to be compressed somehow to fit it on the screen or hidden until some sort of interaction made it appear. Since the data was inherently meaningless without the questions, I decided that a format that would give full space to the questions and their responses would be best. In the end I went with a simple bar graph normalized to the number of people that answered that question in a meaningful way.   

-Axes and Legends:
Once I decided on the standard bar chart, I also decided that I would forego an explicit Y-axis. In all cases, there would be enough width that I could instead include the percentage values on top of each bar. Unless there are many bars, I have generally preferred to show the numbers in this way as it requires far less effort on the part of the reader to get details. I also decided that the visualization was simple enough that a legend was not necessary. 

-Interaction:
Since I was giving each question the full SVG window, it was evident from the beginning that I would need to allow users to scroll through the data. My initial idea was to include arrows above the chart that would allow users to move from one question to the next

-Narrative:
From the beginning, my intention was to create a martini-glass style visualization where I would initially run users through an optional narrative with the data and then allow them to freely explore the data. To this end, I decided to pick some of the bar charts and explore a story with them. 

-Animation
As animation is one of the (many) strengths of D3, I wanted to include animation in a way that would enhance the visualization. I decided to have the bars go down to the X-axis and reemerge with the new data values between every question. I chose this movement to accentuate the fact that there is no direct connection between one question and the next in general. 

Feedback

Offline Feedback
1) One of the first pieces of feedback was that it was nice to be able to move between the questions one at a time, but that it would be helpful to be able to move faster through the dataset.

Solution: I decided to include a quick access bar at the top. I divided the questions into five buckets based on their content. By clicking on the name of the bucket, it would take you to the first question in that bucket. While this doesn't allow quick access to an individual question, it will get you to the right ballpark. As an added benefit, I found that the bar also helped to conceptualize the questions into various groups.

2) During the narrative section in the project, it was pointed out to me that calling out the data that was specifically being referenced in a given dialog box in the presentation would be helpful.

Solution: I added an animation that turns the relevant bars a deeper shade of green shortly after the bars emerge.

Online Feedback
3) On one chart in particular, I was told that it would be helpful to reorder bars so that they are ordered from greatest to least.

Solution: I ordered the bars on that line from greatest to least

Resources: