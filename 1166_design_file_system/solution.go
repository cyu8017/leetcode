// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

type FileSystem struct {
	vals map[string]int
}

func Constructor() FileSystem {
	return FileSystem{vals: map[string]int{}}
}

func (this *FileSystem) CreatePath(path string, value int) bool {
	if path == "/" {
		return false
	}
	if _, exists := this.vals[path]; exists {
		return false
	}
	parent := path
	for i := len(path) - 1; i >= 0; i-- {
		if path[i] == '/' {
			parent = path[:i]
			break
		}
	}
	if parent != "" {
		if _, ok := this.vals[parent]; !ok {
			return false
		}
	}
	this.vals[path] = value
	return true
}

func (this *FileSystem) Get(path string) int {
	if v, ok := this.vals[path]; ok {
		return v
	}
	return -1
}
