select user_id,name,mail
from users
where 
 mail regexp '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$' 
 and mail like binary '%@leetcode.com';
/*regexp allows you to match complex text patterns that cannot be checked using simple operators like LIKE.
Syntax:column_name REGEXP 'pattern'
Breakdown:
^ → start
[A-Za-z] → must start with a letter
[A-Za-z0-9._-]* → allowed characters
@leetcode\.com → domain must match
$ → end
*/
