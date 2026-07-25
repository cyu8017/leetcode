// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

type ThroneInheritance struct {
	king     string
	children map[string][]string
	dead     map[string]bool
}

func Constructor(kingName string) ThroneInheritance {
	return ThroneInheritance{
		king:     kingName,
		children: make(map[string][]string),
		dead:     make(map[string]bool),
	}
}

func (this *ThroneInheritance) Birth(parentName string, childName string) {
	this.children[parentName] = append(this.children[parentName], childName)
}

func (this *ThroneInheritance) Death(name string) {
	this.dead[name] = true
}

func (this *ThroneInheritance) GetInheritanceOrder() []string {
	order := []string{}
	var visit func(string)
	visit = func(name string) {
		if !this.dead[name] {
			order = append(order, name)
		}
		for _, child := range this.children[name] {
			visit(child)
		}
	}
	visit(this.king)
	return order
}
