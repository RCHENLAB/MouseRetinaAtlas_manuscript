#!/usr/bin/env python3
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import sys
import pandas as pd
import scanpy as sc
if __name__ == '__main__':
	x=sc.read(f)
	if raw:
		x=x.raw.to_adata()
	if norm:
		sc.pp.normalize_total(x)
	if log1p:
		sc.pp.log1p(x)
	print('==> x.var.index')
	print(x.var.index)

	marker=pd.read_csv(marker, sep='\t', header=None)
	print('==> marker')
	print(marker)

	if marker.shape[1]==2:
		marker=marker[marker[1].isin(x.var.index)]
		marker=marker.groupby(0).apply(lambda x: x[1].tolist()).to_dict()
	else:
		marker=marker[0]
		marker=marker[marker.isin(x.var.index)]
	print('==> marker subset')
	print(marker)

	categoryorder=None
	if order!='':
		categoryorder=pd.read_csv(order, sep='\t', header=None)[0]

	title=title if title!='' else None
	sc.set_figure_params(dpi_save=500, figsize=(width, height))
	sc.pl.dotplot(x, marker, groupby=groupby, categories_order=categoryorder, use_raw=False, dendrogram=dendrogram, mean_only_expressed=meanexpr, log=log, show=False, swap_axes=swapaxes, var_group_rotation=rotate, title=title, save=f'{bname}.pdf')
