package org.maslov.greedy;

import java.util.Arrays;

public class NonOverlapingIntervals {
//    https://leetcode.com/problems/non-overlapping-intervals/


    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(v1, v2)->(v1[1]-v2[1]));
        int count = 1;
        int end = intervals[0][1];
        for(int i=1;i<intervals.length;i++){
            if(intervals[i][0]>=end){
                count++;
                end = intervals[i][1];
            }
        }
        return intervals.length-count;
    }
}
