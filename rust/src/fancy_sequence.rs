struct Fancy {
    data: Vec<i128>, //i128 for maximum size
    operations: Vec<(char, i128, usize)>,
}

impl Fancy {
    fn new() -> Self {
        return Fancy {
            data: vec![],
            operations: vec![],
        };
    }

    fn append(&mut self, val: i32) {
        self.data.push(val as i128); //add to end of list
    }

    fn add_all(&mut self, inc: i32) {
        self.operations
            .push(('+', inc as i128, self.data.len() - 1)); // add "+ inc" to the list of operations todo, apply only on current data
    }

    fn mult_all(&mut self, m: i32) {
        self.operations.push(('*', m as i128, self.data.len() - 1)); // add "* m" to the list of operations todo, apply only on current data
    }

    fn get_index(&self, idx: i32) -> i32 {
        if idx as usize >= self.data.len() {
            //if out of bounds, return -1
            return -1;
        }

        let mut value = self.data[idx as usize];
        for (operation, amount, until_index) in self.operations.clone() {
            if idx as usize > until_index {
                // if operation came before data, ignore step
                continue;
            }

            if operation == '+' {
                value += amount
            } else {
                value *= amount
            }
        }

        return (value % 1000000007) as i32; //return value with modulo 10^9 + 7
    }
}
