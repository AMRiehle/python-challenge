# python-challenge
GWU Data Analytics Bootcamp Homework 3

This repository contains the code and output for homework assignments issued through the GWU Data Analytics Bootcamp as part of their Beginning Python module. Brief descriptions of each challenge are provided below:

## PyBank

The goal of this challenge was to take a dataset consisting of "Date" and "Revenue" fields and return:

* The total number of months included in the dataset

* The total amount of revenue generated over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

## PyPoll

The goal of this challenge was to take a dataset consisting of "Voter ID", "County", and "Candidate" fields and return:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

While present, the "County" information was a red herring for this challenge.

## PyBoss

The goal of this challenge was to convert data from one format to another. Specifically, we were looking to convert data from the following format:

```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

To the following format:


```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

## PyParagraph

The goal of this challenge was to assess a paragraph for the following:

* Approximate word count

* Approximate sentence count

* Average letter count (per word)

* Average sentence length (in words)

I was not able to determine what to do in a case where a paragraph includes a period as part of a person's name (e.g., Ms. Anna M. Riehle), but the code should otherwise work correctly.
