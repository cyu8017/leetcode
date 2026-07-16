// LeetCode 0341 - Flatten Nested List Iterator

// https://leetcode.com/problems/flatten-nested-list-iterator/



import java.util.ArrayDeque;

import java.util.ArrayList;

import java.util.Deque;

import java.util.List;



class NestedInteger {

    private Integer integer;

    private final List<NestedInteger> list = new ArrayList<>();



    public NestedInteger() {}



    public NestedInteger(int value) {

        this.integer = value;

    }



    public boolean isInteger() {

        return integer != null;

    }



    public int getInteger() {

        return integer != null ? integer : 0;

    }



    public List<NestedInteger> getList() {

        return list;

    }

}



class NestedIterator {

    private static class Entry {

        NestedInteger node;

        int index;



        Entry(NestedInteger node, int index) {

            this.node = node;

            this.index = index;

        }

    }



    private final Deque<Entry> stack = new ArrayDeque<>();



    public NestedIterator(List<NestedInteger> nestedList) {

        for (int index = nestedList.size() - 1; index >= 0; index--) {

            stack.push(new Entry(nestedList.get(index), 0));

        }

    }



    public int next() {

        Entry current = stack.pop();

        if (current.node.isInteger()) {

            return current.node.getInteger();

        }

        return advance(current.node.getList());

    }



    public boolean hasNext() {

        prepareNext();

        return !stack.isEmpty();

    }



    private void prepareNext() {

        while (!stack.isEmpty()) {

            Entry top = stack.peek();

            NestedInteger current = top.node;

            if (current.isInteger()) {

                return;

            }



            List<NestedInteger> nested = current.getList();

            if (top.index >= nested.size()) {

                stack.pop();

                continue;

            }



            top.index++;

            stack.push(new Entry(nested.get(top.index - 1), 0));

        }

    }



    private int advance(List<NestedInteger> nested) {

        for (int index = nested.size() - 1; index >= 0; index--) {

            stack.push(new Entry(nested.get(index), 0));

        }

        prepareNext();

        Entry current = stack.pop();

        if (current.node.isInteger()) {

            return current.node.getInteger();

        }

        return advance(current.node.getList());

    }

}
