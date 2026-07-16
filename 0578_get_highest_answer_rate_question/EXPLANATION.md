# How We Solve Get Highest Answer Rate Question

Answer rate is answers divided by shows; break ties by smallest question id.

## Steps

1. Group `SurveyLog` by `question_id`.
2. Compute `answer_count / show_count`.
3. Order by rate descending, then question id, and take the first.
