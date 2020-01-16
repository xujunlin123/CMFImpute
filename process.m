function [processed_data] = process(data)

data=data';
min_count=0; min_cells=2;
  
%% Removing BAD genes
cs= sum(data>min_count);
x_use_genes = find(cs>min_cells);

gene_filtered_data=data(:,x_use_genes);


%% Median normalization
% libsize  = sum(gene_filtered_data,2);
%  
% gene_filtered_data = bsxfun(@rdivide, gene_filtered_data, libsize) * median(libsize);

%% Log transform
processed_data = log10(1+gene_filtered_data);
end

