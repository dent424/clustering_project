Readme File for Alex Moore's Data Visualization Project

A note on folder names - You may see the word cluster around the files. This is because these visualizations are the first part of a larger project involving clustering. These clusters are not currently implemented.

Folders:
Data Cleaning Tools - This folder contains tools used to clean and reformat the data in preparation for creating a D3 data visualization
Original Data - Contains the original data which was cleaned as well as supporting documents for the data
Visualization Text - Contains text used in the visualization

Important Files
clusterData.csv - Data used in visualization
index.html - main visualization


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
1) One of the first pieces of feedback was that it was nice to be able to move between the questions one at a time, but that it would be helpful to be able to move faster through the dataset. (See index-before-chapters.html)

Solution: I decided to include a quick access bar at the top. I divided the questions into five buckets based on their content. By clicking on the name of the bucket, it would take you to the first question in that bucket. While this doesn't allow quick access to an individual question, it will get you to the right ballpark. As an added benefit, I found that the bar also helped to conceptualize the questions into various groups.

2) During the narrative section in the project, it was pointed out to me that calling out the data that was specifically being referenced in a given dialog box in the presentation would be helpful. (See index-before-reorder.html)

Solution: I added an animation that turns the relevant bars a deeper shade of green shortly after the bars emerge.

Online Feedback
3) On one chart in particular, I was told that it would be helpful to reorder bars so that they are ordered from greatest to least. (See index-before-reorder.html)

Solution: I ordered the bars on that line from greatest to least

Resources:

CSS
http://stackoverflow.com/questions/13867717/how-to-make-divs-percentage-width-relative-to-parent-div-and-not-viewport
http://www.w3schools.com/cssref/pr_dim_min-width.asp

Python
http://stackoverflow.com/questions/1165352/calculate-difference-in-keys-contained-in-two-python-dictionaries/1165552#1165552

D3 Basics
http://alignedleft.com/tutorials/d3/using-your-data
https://www.dashingd3js.com/svg-text-element
http://stackoverflow.com/questions/13615381/d3-add-text-to-circle
http://www.d3noob.org/2014/02/d3js-elements.html
http://alignedleft.com/tutorials/d3/axes
http://stackoverflow.com/questions/10939082/d3-javascript-alternate-colors-on-click
https://www.dashingd3js.com/svg-group-element-and-d3js
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
http://leaena.com/2014/01/d3-js-rollups/

D3 Example Code
http://bl.ocks.org/mbostock/3886208
https://dev.socrata.com/consumers/examples/simple-chart-with-d3.html
http://bl.ocks.org/mbostock/3885304
http://bl.ocks.org/guilhermesimoes/be6b8be8a3e8dc2b70e2
http://stackoverflow.com/questions/27500617/d3-js-enter-update-exit-with-group-element-in-between
https://github.com/mbostock/d3/wiki/SVG-Axes
http://stackoverflow.com/questions/23459834/why-does-this-d3-code-add-the-p-element-outside-the-body-instead-of-inside-it

Javascript Basics
http://stackoverflow.com/questions/3895478/does-javascript-have-a-method-like-range-to-generate-an-array-based-on-suppl
http://www.w3schools.com/jsref/jsref_toprecision.asp
http://stackoverflow.com/questions/1789945/how-can-i-check-if-one-string-contains-another-substring
http://stackoverflow.com/questions/7342957/how-do-you-round-to-1-decimal-place-in-javascript
http://stackoverflow.com/questions/7346827/javascript-find-array-index-with-value
http://stackoverflow.com/questions/10192662/js-how-to-check-if-a-variable-is-not-undefined
http://stackoverflow.com/questions/5963182/how-to-remove-spaces-from-a-string-using-javascript

My own stackoverflow questions
http://stackoverflow.com/questions/33572531/ignoring-a-group-with-the-d3-nest-function
http://stackoverflow.com/questions/33579449/cant-get-exit-and-enter-to-work-properly-when-updating-data-in-d3-js
