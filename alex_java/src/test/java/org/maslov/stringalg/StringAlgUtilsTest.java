package org.maslov.stringalg;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StringAlgUtilsTest {

    @Test
    void buildZfunction() {
        String s = "aabcaabxaaz";
        var rv = StringAlgUtils.build_Z_function(s);
        int[] expArr = new int[]{0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0};
        assertEquals(s.length(), rv.length);
        assertEquals(3, rv[4]);
        assertEquals(1, rv[5]);
        assertEquals(0, rv[6]);
        assertEquals(0, rv[7]);
        assertEquals(2, rv[8]);
        assertArrayEquals(expArr, rv);

    }
}