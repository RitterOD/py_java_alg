package org.maslov.greedy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ArrayPartitionTest {

    @Test
    void arrayPairSum() {
        int[] test1 = {1, 4, 3, 2};
        ArrayPartition ap = new ArrayPartition();
        int solutionTest1 = ap.arrayPairSum(test1);
        assertEquals(4, solutionTest1);
    }

    @Test
    void arrayPairSumSecondExample() {
        ArrayPartition ap = new ArrayPartition();
        int[] test2 = {6, 2, 6, 5, 1, 2};
        int solutionTest2 = ap.arrayPairSum(test2);
        assertEquals(9, solutionTest2);
    }
}