class BrowserHistory {
    history: any;
    index: any;
    constructor(homepage: any) {

        this.history = [homepage];
        this.index = 0;
    }
    visit(url: any): any {

        this.history.length = this.index + 1;
        this.history.push(url);
        this.index++;
    }
    back(steps: any): any {

        this.index = Math.max(0, this.index - steps);
        return this.history[this.index];
    }
    forward(steps: any): any {

        this.index = Math.min(this.history.length - 1, this.index + steps);
        return this.history[this.index];
    }
}
