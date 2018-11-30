select contest_id, hacker_id, name
, sum(total_submissions), total_accepted_submissions
, total_views, total_unique_views


 from contests, colleges, challenges,submission_stats, view_stats
where (contests.contest_id=colleges.contest_id)
and (college.college_id=challenges.college_id)
and (challenges.challenge_id=submission_stats.challenge_id)
and (challenges.challenge_id=view_statis.challenge_id)
order by contest_id
