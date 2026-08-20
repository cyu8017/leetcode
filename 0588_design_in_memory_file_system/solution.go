// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

import "sort"

type FileSystem struct {
	root map[string]any
}

func Constructor() FileSystem {
	return FileSystem{root: map[string]any{}}
}

func (fs *FileSystem) parts(path string) []string {
	raw := splitPath(path)
	out := []string{}
	for _, p := range raw {
		if p != "" {
			out = append(out, p)
		}
	}
	return out
}

func splitPath(path string) []string {
	parts := []string{}
	cur := ""
	for i := 0; i < len(path); i++ {
		if path[i] == '/' {
			parts = append(parts, cur)
			cur = ""
		} else {
			cur += string(path[i])
		}
	}
	parts = append(parts, cur)
	return parts
}

func (fs *FileSystem) Ls(path string) []string {
	if path == "/" {
		keys := make([]string, 0, len(fs.root))
		for k := range fs.root {
			keys = append(keys, k)
		}
		sort.Strings(keys)
		return keys
	}
	parts := fs.parts(path)
	var node any = fs.root
	for _, part := range parts {
		node = node.(map[string]any)[part]
	}
	if s, ok := node.(string); ok {
		_ = s
		return []string{parts[len(parts)-1]}
	}
	m := node.(map[string]any)
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

func (fs *FileSystem) Mkdir(path string) {
	node := fs.root
	for _, part := range fs.parts(path) {
		next, ok := node[part]
		if !ok {
			next = map[string]any{}
			node[part] = next
		}
		node = next.(map[string]any)
	}
}

func (fs *FileSystem) AddContentToFile(filePath string, content string) {
	parts := fs.parts(filePath)
	node := fs.root
	for _, part := range parts[:len(parts)-1] {
		next, ok := node[part]
		if !ok {
			next = map[string]any{}
			node[part] = next
		}
		node = next.(map[string]any)
	}
	name := parts[len(parts)-1]
	existing, _ := node[name].(string)
	node[name] = existing + content
}

func (fs *FileSystem) ReadContentFromFile(filePath string) string {
	parts := fs.parts(filePath)
	var node any = fs.root
	for _, part := range parts {
		node = node.(map[string]any)[part]
	}
	return node.(string)
}
