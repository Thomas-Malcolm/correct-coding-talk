/* swaps pointers for `a` and `b`
 * Requires: *a,*b are pointers with *a = old(*a) and *b = old(*b)
 * Ensures: *a,*b are pointers with *a = old(*b) and *b = old(*a)
 */
void swap(void** a, void** b) {

    // *b = 
    void* bTmp = *b;
    // bTmp = old(*a) && *a = old(bTmp)
    *b = *a;
    // bTmp = old(*b) && *b = old(bTmp)
    *a = bTmp;
    // *a = old(*b) && *b = old(*a)
}
