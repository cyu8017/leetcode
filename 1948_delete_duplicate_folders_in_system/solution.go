// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

import "sort"

type folderNode struct {
	children map[string]*folderNode
}

func deleteDuplicateFolder(paths [][]string) [][]string {
	root := &folderNode{children: make(map[string]*folderNode)}
	for _, path := range paths {
		node := root
		for _, folder := range path {
			if node.children[folder] == nil {
				node.children[folder] = &folderNode{children: make(map[string]*folderNode)}
			}
			node = node.children[folder]
		}
	}
	dup := make(map[string]bool)
	serialOf := make(map[*folderNode]string)

	var serialize func(node *folderNode) string
	serialize = func(node *folderNode) string {
		if len(node.children) == 0 {
			return ""
		}
		names := make([]string, 0, len(node.children))
		for name := range node.children {
			names = append(names, name)
		}
		sort.Strings(names)
		parts := make([]byte, 0)
		for _, name := range names {
			parts = append(parts, name...)
			parts = append(parts, '(')
			parts = append(parts, serialize(node.children[name])...)
			parts = append(parts, ')')
		}
		serial := string(parts)
		if serial != "" {
			if _, ok := dup[serial]; ok {
				dup[serial] = true
			} else {
				dup[serial] = false
			}
			serialOf[node] = serial
		}
		return serial
	}
	serialize(root)

	ans := [][]string{}
	var collect func(node *folderNode, path []string)
	collect = func(node *folderNode, path []string) {
		for name, child := range node.children {
			serial := serialOf[child]
			if serial != "" && dup[serial] {
				continue
			}
			path = append(path, name)
			cp := make([]string, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			collect(child, path)
			path = path[:len(path)-1]
		}
	}
	collect(root, nil)
	return ans
}
