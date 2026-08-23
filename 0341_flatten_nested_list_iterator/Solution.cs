// LeetCode 0341 - Flatten Nested List Iterator

// https://leetcode.com/problems/flatten-nested-list-iterator/



using System.Collections.Generic;



public class NestedInteger {

    private int? integer;

    private readonly List<NestedInteger> list = new();



    public NestedInteger() {}



    public NestedInteger(int value) {

        integer = value;

    }



    public bool IsInteger() {

        return integer.HasValue;

    }



    public int GetInteger() {

        return integer ?? 0;

    }



    public IList<NestedInteger> GetList() {

        return list;

    }

}



public class NestedIterator {

    private sealed class Entry {

        public NestedInteger Node;

        public int Index;



        public Entry(NestedInteger node, int index) {

            Node = node;

            Index = index;

        }

    }



    private readonly Stack<Entry> stack = new();



    public NestedIterator(IList<NestedInteger> nestedList) {

        for (int index = nestedList.Count - 1; index >= 0; index--) {

            stack.Push(new Entry(nestedList[index], 0));

        }

    }



    public int Next() {

        Entry current = stack.Pop();

        if (current.Node.IsInteger()) {

            return current.Node.GetInteger();

        }

        return Advance(current.Node.GetList());

    }



    public bool HasNext() {

        PrepareNext();

        return stack.Count > 0;

    }



    private void PrepareNext() {

        while (stack.Count > 0) {

            Entry top = stack.Peek();

            NestedInteger current = top.Node;

            if (current.IsInteger()) {

                return;

            }



            IList<NestedInteger> nested = current.GetList();

            if (top.Index >= nested.Count) {

                stack.Pop();

                continue;

            }



            top.Index++;

            stack.Push(new Entry(nested[top.Index - 1], 0));

        }

    }



    private int Advance(IList<NestedInteger> nested) {

        for (int index = nested.Count - 1; index >= 0; index--) {

            stack.Push(new Entry(nested[index], 0));

        }

        PrepareNext();

        Entry current = stack.Pop();

        if (current.Node.IsInteger()) {

            return current.Node.GetInteger();

        }

        return Advance(current.Node.GetList());

    }

}
