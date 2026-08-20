// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/


type EventEmitter struct {
	handlers map[string][]func([]interface{})
}

func Constructor() EventEmitter {
	return EventEmitter{handlers: map[string][]func([]interface{}){}}
}

func (e *EventEmitter) Subscribe(eventName string, callback func([]interface{})) func() {
	e.handlers[eventName] = append(e.handlers[eventName], callback)
	idx := len(e.handlers[eventName]) - 1
	return func() {
		if idx >= 0 && idx < len(e.handlers[eventName]) {
			e.handlers[eventName] = append(e.handlers[eventName][:idx], e.handlers[eventName][idx+1:]...)
			idx = -1
		}
	}
}

func (e *EventEmitter) Emit(eventName string, args []interface{}) []interface{} {
	res := []interface{}{}
	for _, cb := range e.handlers[eventName] {
		cb(args)
		res = append(res, nil)
	}
	return res
}
