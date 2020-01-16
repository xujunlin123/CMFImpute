function [score]=SM(A)

[m,n]=size(A);
%D =pdist(A,'correlation');
D=pdist(A,'euclidean');
%D =pdist(A,'chebychev');
score=zeros(m,m);
n=1;
for i=1:m
    for j=i+1:m
        score(i,j)=D(1,n);
        n=n+1;
    end
end
score=score./max(max(score));
score=score+score';
score=score./max(max(score));
score=1./(score+1);

end

