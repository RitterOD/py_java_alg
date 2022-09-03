package org.maslov.greedy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class NonOverlapingIntervalsTest {

    @Test
    void eraseOverlapIntervals() {

        int[][] intervals = {{1,2},{2,3},{3,4},{1,3}};
        NonOverlapingIntervals solution = new NonOverlapingIntervals();

        int rv = solution.eraseOverlapIntervals(intervals);
        assertEquals(1, rv);
    }

    @Test
    void eraseOverlapIntervalsCase2() {

        int[][] intervals = {{1,2},{1,2}, {1,2}};
        NonOverlapingIntervals solution = new NonOverlapingIntervals();

        int rv = solution.eraseOverlapIntervals(intervals);
        assertEquals(2, rv);
    }

    @Test
    void eraseOverlapIntervalsCase3() {

        int[][] intervals = {{1,2},{2,3}};
        NonOverlapingIntervals solution = new NonOverlapingIntervals();

        int rv = solution.eraseOverlapIntervals(intervals);
        assertEquals(0, rv);
    }
}