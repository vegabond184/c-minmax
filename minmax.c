#include <stdio.h>
#include <stdlib.h>

/*
 * Program: Custom Min and Max Functions in C
 *
 * Description:
 * This code defines two functions:
 *   1. findMin() → Finds and returns the smallest element in an integer array.
 *   2. findMax() → Finds and returns the largest element in an integer array.
 *
 * Both functions loop through the array manually instead of using built-in
 * helpers, making it a clear demonstration of how min/max can be implemented.
 *
 * Author: [Prateek Yadav]
 * Date: [30-8-2025]
 */

/*
 * Function: findMin
 * -----------------
 * Finds the minimum (smallest) value in an array of integers.
 *
 * numbers: The input integer array
 * length:  The number of elements in the array
 *
 * returns: The smallest integer value in the array
 */
int findMin(int numbers[], int length) {
    int minValue = numbers[0];  // Assume the first element is the minimum initially

    for (int index = 0; index < length; index++) {
        if (minValue > numbers[index]) {  // If a smaller element is found
            minValue = numbers[index];    // Update minValue
        }
    }
    return minValue;  // Return the smallest element found
}

/*
 * Function: findMax
 * -----------------
 * Finds the maximum (largest) value in an array of integers.
 *
 * numbers: The input integer array
 * length:  The number of elements in the array
 *
 * returns: The largest integer value in the array
 */
int findMax(int numbers[], int length) {
    int maxValue = numbers[0];  // Assume the first element is the maximum initially

    for (int index = 0; index < length; index++) {
        if (maxValue < numbers[index]) {  // If a larger element is found
            maxValue = numbers[index];    // Update maxValue
        }
    }
    return maxValue;  // Return the largest element found
}


