package org.maslov.graph.sametree;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class SameTreeTest {

    @Test
    public void isSameTree() {
        TreeNode tn1 = new TreeNode(1);
        TreeNode tn2 = new TreeNode(2);
        TreeNode tn3 = new TreeNode(3);
        tn1.left = tn2;
        tn1.right = tn3;

        TreeNode t2n1 = new TreeNode(1);
        TreeNode t2n2 = new TreeNode(2);
        TreeNode t2n3 = new TreeNode(3);
        t2n1.left = t2n2;
        t2n1.right = t2n3;
        boolean rv = SameTree.isSameTree(tn1, t2n1);
        assertTrue(rv);
    }

    @Test
    public void isSameTree2example() {
        TreeNode t1n1 = new TreeNode(1);
        TreeNode t1n2 = new TreeNode(2);

        t1n1.left = t1n2;


        TreeNode t2n1 = new TreeNode(1);
        TreeNode t2n2 = new TreeNode(2);

        t2n1.right = t2n2;
        boolean rv = SameTree.isSameTree(t1n1, t2n1);
        assertFalse(rv);
    }


    @Test
    public void isSameTree3example() {
        TreeNode t1n1 = new TreeNode(1);
        TreeNode t1n2 = new TreeNode(2);
        TreeNode t1n3 = new TreeNode(1);
        t1n1.left = t1n2;
        t1n1.right = t1n3;

        TreeNode t2n1 = new TreeNode(1);
        TreeNode t2n2 = new TreeNode(1);
        TreeNode t2n3 = new TreeNode(2);
        t2n1.left = t2n2;
        t2n1.right = t2n3;
        boolean rv = SameTree.isSameTree(t1n1, t2n1);
        assertFalse(rv);
    }

}