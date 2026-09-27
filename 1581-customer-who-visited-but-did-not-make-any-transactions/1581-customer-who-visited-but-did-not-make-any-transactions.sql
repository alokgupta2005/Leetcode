# Write your MySQL query statement below
select visits.customer_id , COUNT(*) AS count_no_trans
from visits
left join transactions
on visits.visit_id = transactions.visit_id
where  Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id;