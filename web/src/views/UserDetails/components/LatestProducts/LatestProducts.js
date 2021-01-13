import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import PerfectScrollbar from 'react-perfect-scrollbar';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardContent,
  CardHeader,
  Divider,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TableSortLabel,
  Tooltip,
} from '@material-ui/core';
import axios from 'utils/axios';
import { GenericMoreButton } from 'components';

const useStyles = makeStyles(theme => ({
  root: {},
  content: {
    padding: 0
  },
  inner: {
    minWidth: 700
  },
  progressContainer: {
    padding: theme.spacing(3),
    display: 'flex',
    justifyContent: 'center'
  },
  actions: {
    justifyContent: 'flex-end'
  },
  arrowForwardIcon: {
    marginLeft: theme.spacing(1)
  }
}));


const LatestProducts = props => {
  const { className, id, ...rest } = props;

  const classes = useStyles();
  const [sales, setSales] = useState(null);

  useEffect(() => {
    let mounted = true;

    const fetchSales = () => {
      axios.get('/user/'+ id +'/sales/').then(response => {
        if (mounted) {
          setSales(response.data.sales);
        }
      });
    };

    fetchSales();

    return () => {
      mounted = false;
    };
  }, [id]);

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <CardHeader
        action={<GenericMoreButton />}
        title="Latest Products"
      />
      <Divider />
      <CardContent className={classes.content}>
        <PerfectScrollbar options={{ suppressScrollY: true }}>
          <div className={classes.inner}>
            {sales && (
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell sortDirection="desc">
                      <Tooltip
                        enterDelay={300}
                        title="Product"
                      >
                        <TableSortLabel
                          active
                          direction="desc"
                        >
                          Product
                        </TableSortLabel>
                      </Tooltip>
                    </TableCell>
                    <TableCell>Quantity</TableCell>
                    <TableCell>Sale</TableCell>
                    <TableCell>Data</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {sales.map(sales => (
                    <TableRow
                      hover
                      key={sales.id}
                    >
                      <TableCell>{sales.product.name}</TableCell>
                      <TableCell>{sales.quantity}</TableCell>
                      <TableCell>{'$ '}{sales.total}</TableCell>
                      <TableCell>{sales.date}</TableCell>                      
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            )}
          </div>
        </PerfectScrollbar>
      </CardContent>      
    </Card>
  );
};

LatestProducts.propTypes = {
  className: PropTypes.string,
  id: PropTypes.number
};

export default LatestProducts;
