with clean_data as (
Select task_id,
predicted_label,
confidence_score
from model_outputs
where confidence_score>0.5
)
select b.category,
count(*) as total_items,
sum( case when b.actual_label != c.predicted_label then 1 else 0 end ) as total_errors,
avg( case when b.actual_label != c.predicted_label then c.confidence_score else null end ) as avg_false_confidence
from benchmark_labels b
join clean_data c on b.task_id=c.task_id
where b.is_edge_case = TRUE
GROUP BY b.category
having count(*) > 	1
order by total_errors desc;




