<!-- Random-Book-Data-Generator -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">Random-Book-Data-Generator</h3>

  <p align="center">This project is a part of making a system that suggests queries. Here, we mostly worked on making the data set that will be   used in the project.
    <br />
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project is a part of making a system that suggests queries. Here, we focused mostly on assembling the dataset that will be utilized for the project.
Regarding the construction of the \textbf{synthetic dataset}, it generates a csv file named "book\_dataset.csv" with a random book dataset. It utilizes the "Faker" library to generate fictitious data such as the book's title, author, ISBN number, release date, etc.
\\
It begins by opening a new csv file titled "random\_books.csv," starting a csv writer, and writing the header row containing the field names. Then, the "Faker" library generates 20,000 rows of fake data and writes each row to the CSV file.The file is then renamed from "random books.csv" to "book dataset.csv." Following this, we constructed the user id set, the query set, and the utility matrix in the same manner as for our actual dataset.

Here's why we created four types of dataset here:
* A relational table populated with tuples. The table is expressed as a CSV file, where each row is a tuple, and the first row contains the names of the fields (attributes). You can assume that there are no NULL values. All the fields of all the tuples have a value. 
* A user set. A user set was then built. The collection of users consists of merely an array of ids. This data is provided in a file format, with one user ID per line.
* A query set, which is a set of queries that have been posed in the past. Each query has a unique query id and its definition (i.e., the set of conditions). The query set is expressed as a CSV file where each line contains the conditions attribute=value separated by comma. The first element of each row is a query id. For example, a row in the query set is: 
Q1821, author=John, genre=fantasy
* A utility matrix User-Query that has for certain combinations of user and query, the User-Query utility matrix contains, for each combination of user and query, a value between 1 and 100 that represents the user's level of satisfaction with the result set for that query. This is also offered as a CSV file, with the first row including a list of query ids separated by commas. Each alternate row begins with a userId, then a sequence of fields separated by commas (as many as the number of query names of the first row). These fields may be left empty or populated with numbers between 1 and 100. We created this file with 20% missing value.


### Built With
* [Python][ https://www.python.org/ ][ Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

