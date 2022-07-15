package org.maslov.stringalg;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class StringAlgUtils {
    public static int[] build_Z_function(String s) {
        var rv = new int[s.length()];

        int k = 1;
        // exactly left index of most right block
        int l = 0;
        // exactly right index of most right block
        int r = 0;
        while(k < s.length() - 1) {
            if (r < k) {
                int cur_z = 0;
                while(k + cur_z < s.length() && s.charAt(cur_z) == s.charAt(k + cur_z)) {
                    ++cur_z;
                }
                rv[k] = cur_z;
                if (cur_z != 0) {
                    l = k;
                    r = k + cur_z - 1;
                }
            } else {
                int k_tmp = k - l;
                int b_len = r - k + 1;
                if (b_len > rv[k_tmp]) {
                    rv[k] = rv[k_tmp];
                } else {
                    int cnt = 0;
                    while(r + cnt <= s.length() - 1) {
                        if (s.charAt(r + cnt) == s.charAt(b_len + 1)) {
                            cnt++;
                        } else {
                            rv[k] = r - k + 1  + cnt ;
                            r = r + cnt;
                            l = k;
                            break;
                        }
                    }
                }
            }
            ++k;
        }
        return rv;
    }

    public static List<Integer> findPatterns(String text, String pattern) {
        char delimeter = '!';
        if (text.chars().filter(e -> e == delimeter).count() != 0) {
            throw new IllegalArgumentException("text contains delimeter symbol !. Change delimeter symbol");
        }
        if (pattern.chars().filter(e -> e == delimeter).count() != 0) {
            throw new IllegalArgumentException("pattern contains delimeter symbol !. Change delimeter symbol");
        }
        String procText = pattern + delimeter + text;
        int[] z = build_Z_function(procText);
        var rv = new ArrayList<Integer>();
        for(int i = pattern.length() + 1; i < procText.length(); ++i) {
            if(z[i] == pattern.length()) {
                rv.add(i - pattern.length() - 1);
            }
        }
        return rv;
    }

}
