select 
sum(out_time-in_time) as total_time,
emp_id,
event_day as day
from employees
group by event_day,emp_id
