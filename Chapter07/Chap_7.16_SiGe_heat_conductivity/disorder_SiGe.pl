#!perl
use strict;
use Getopt::Long;
use MaterialsScript qw(:all);
my $disorderedStructure = $Documents{"SiGe.xsd"};
my $results = Tools->Disorder->StatisticalDisorder
   ->GenerateSuperCells
($disorderedStructure,1,1,1);
my $table = $results->StudyTable;
