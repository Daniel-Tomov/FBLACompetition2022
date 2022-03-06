# FBLACompetition2022

This is a program for the FBLA 2022 Programming Competition. The task is to create a program that suggests attractions to potential visitors. The program should allow users to search for attractions in the area based on desired attributes. The program should include at least 50 attractions, and users must be able to define at least five desired attributes to search for an attraction.

https://www.fbla-pbl.org/fbla-topics Then select "Coding & Programming"

# How it works:

At startup, a list is created with different classes. Inside each class, there is an attraction with different attributes. Attributes include the attraction's address, website, tags to filter, image, and name. After they are loaded into classes, the different regions and tags are loaded into two separate lists, <b>provinceList</b> and <b>filters</b> respectively, to make the inputing of new attractions simple. In other words, as more attractions are added, the filters and provinces update with the attractions automatically. In addition, there is a <b>checkList</b> that contains the check status of the provinces and the tags. There is also antoher list that stores the attractions and is not edited.

<h3>GET request (page load that does not use "Apply Filters" button)</h3>
Everytime a user loads the webpage normally (they are not submitting a request), the non-changing list is sent. The <b>checkList</b> is cleared so no tags or provinces are checked. This should decrease the loading of the webpage on first load because almost no is being changed. 

<h3>POST request (every page load that uses "Apply Filters" button</h3>
On a POST request, the first thing that is done is the program checks if the "Apply Filters" button was used. Then checks for which tags were checked and the appropriate attractions are removed from the <b>returnList</b>. There are also checks for which province was checked and the provinces that are not that province are removed. The <b>checkList</b> is contains the check status of the filters and provinces at the same index as the filters and provinces. In the <b>checkList</b>, the filters are first and then the provinces. The <b>returnList</b> now contains only the attractions that fit the criteria of the tags and provinces the user picked. This list is returned along with the <b>filters</b>, <b>provinceList</b>, and <b>checkList</b>.

# Python Dependencies:

<h3>Flask</h3>
Used to host the website. Responsible for processing the filters the user specified and returning the attractions that match. Also used for key functionality like the "for" loop to add different attractions to webpage with little code and the "if" statement that shows the user if their search criterea does not have any matches.

# Streamed live:

February 4, 2022 - https://youtu.be/yQBg888QrCo

March 5, 2022 - https://youtu.be/kSB46POVrN8


# Images

Images property of the respective attraction.
