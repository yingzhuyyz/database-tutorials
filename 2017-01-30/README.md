## Transactions
# ACID property
- Atomicity
	* Supported by sqlite
- Consistency
- Integrity
	* Supported by sqlite
- Durability

- Supporting all of them is costly.  The user must decide which one to
  give up.

## Transaction isolation level
- Full isolation = `SERIALIZABLE`
- No isolation = `READ UNCOMMITTED`
