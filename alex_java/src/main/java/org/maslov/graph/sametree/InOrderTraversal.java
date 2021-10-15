package org.maslov.graph.sametree;

import java.util.ArrayList;
import java.util.List;

// leetcode Binary Tree Inorder Traversal
public class InOrderTraversal {
    private void treeNodeImp(ArrayList<Integer> lst, TreeNode root) {
        if (root == null) {
            return;
        } else {
            treeNodeImp(lst, root.left);
            lst.add(root.val);
            treeNodeImp(lst, root.right);
        }
    }

    public List<Integer> inorderTraversalSecondSolution(TreeNode root) {
        ArrayList<Integer> rv = new ArrayList<>(100);
        treeNodeImp(rv, root);
        return rv;

    }


    public List<Integer> inorderTraversal(TreeNode root) {
            if (root == null) {
                return new ArrayList<Integer>();
            } else {
                List<Integer> rv  = inorderTraversal(root.left);
                rv.add(root.val);
                rv.addAll(inorderTraversal(root.right));
                return rv;
            }
    }
}
