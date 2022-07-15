package org.maslov.greedy;

import java.util.Arrays;


/*
* link to problem https://leetcode.com/problems/array-partition/
*
* */
public class ArrayPartition {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (i % 2 == 0) {
                sum += nums[i];
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] test1 = {1, 4, 3, 2};
        ArrayPartition ap = new ArrayPartition();
        int solutionTest1 = ap.arrayPairSum(test1);
        System.out.println("Solution test1 = " + solutionTest1);
        int[] test2 = {6, 2, 6, 5, 1, 2};
        int solutionTest2 = ap.arrayPairSum(test2);
        System.out.println("Solution test2 = " + solutionTest2);
    }
}
