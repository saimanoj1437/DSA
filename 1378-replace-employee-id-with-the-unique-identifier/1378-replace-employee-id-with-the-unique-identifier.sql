# Write your MySQL query statement below
select
e.name as name,eu.unique_id as unique_id 

from employees e left join employeeUNI eu on e.id = eu.id