struct Fancy {
    data: Vec<i128>, //i128 for maximum size
}

impl Fancy {
    fn new() -> Self {
        return Fancy { data: vec![] };
    }

    fn append(&mut self, val: i32) {
        self.data.push(val as i128); //add to end of list
    }

    fn add_all(&mut self, inc: i32) {
        for i in 0..self.data.len() { //to every entry, add inc
            self.data[i] += inc as i128;
        }
    }

    fn mult_all(&mut self, m: i32) {
        for i in 0..self.data.len() { // multiply every entry by m
            self.data[i] *= m as i128;
        }
    }

    fn get_index(&self, idx: i32) -> i32 {
        if idx as usize >= self.data.len() { //if out of bounds, return -1
            return -1;
        }

        return (self.data[idx as usize] % 1000000007) as i32; //return value with modulo 10^9 + 7
    }
}
