# CISC 365 Project 1 Report
> Team members: Kyle Verma, Yu Peng, Yu Chen Cai, Yi Kuang, Somion Tian

> I confirm that this submission is our own work and is consistent with the Queen's regulations on Academic Integrity.

## Experiment 1
### Step 1.
We decide to generate every element of list $A^{(n)}$ with every element $A^{(n)}_i$ in the range $A^{(n)}_i \in [0, 4*n] \sub \N$.

The generated array is then sorted ascending with merge sort algorithm.


## Experiment 2

## Question 1: 
### Binary search and trinary search both fall into the O(log n) complexity class. Do your experiments show growth in execution time that is consistent with this?

O(log n) complexity indicates that time will increase linearly as n increases exponentially. With the values given in the experiments they appear to increase by the previous n being multiplied by 2 (n= 1000, n = 2000, n = 4000, n = 8000, n = 16000). With n values like this we would not observe time increasing linearly as n increases exponentially, however if we had say n = 1000000 we would be able to see that compared to n = 1000 time would increase linearly as the increase from 1000 to 1000000 is exponential (n^2).

## Question 2:
### Compare the total time for the two search algorithms:
### - Do they ever differ by more than 10%, or are they always within 10% of eachother?
### - Under what conditions (if any) is binary search at least 10% faster and underwhat conditions (if any) is trinary search at least 10% faster?
