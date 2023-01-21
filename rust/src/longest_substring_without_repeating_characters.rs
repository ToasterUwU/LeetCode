impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut longest_sequence = 0; // return value for later

        let mut counter: i32; // counter for current sequence
        let mut already_saw: String; // storage to check for repeating chars
        for i in 0..s.len() {
            // for every possible startpoint in string
            counter = 0;
            already_saw = String::new();

            for (j, c) in s.chars().enumerate() {
                if j < i {
                    // if we arent at startpoint yet, continue
                    continue;
                }

                if already_saw.contains(c) {
                    // if something repeated, break
                    break;
                }

                counter += 1; //add point
                already_saw.push(c); //put seen char in storage
            }

            if counter > longest_sequence {
                //set new highscore if needed
                longest_sequence = counter
            }
        }

        return longest_sequence;
    }
}
