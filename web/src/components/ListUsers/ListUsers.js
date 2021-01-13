import React from 'react';
import clsx from 'clsx';
import PerfectScrollbar from 'react-perfect-scrollbar';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardActions,
  CardHeader,
  CardContent,
  Divider,
  Table,
  TableRow,
  TableCell,
  Typography,
  colors,
  TableBody
} from '@material-ui/core';

import { GenericMoreButton } from 'components';

const useStyles = makeStyles(theme => ({
  root: {},
  content: {
    padding: 0,
    '&:last-child': {
      paddingBottom: 0
    }
  },
  inner: {
    minWidth: 700
  },
  details: {
    display: 'flex',
    alignItems: 'center'
  },
  image: {
    marginRight: theme.spacing(2),
    flexShrink: 0,
    height: 56,
    width: 56
  },
  subscriptions: {
    fontWeight: theme.typography.fontWeightMedium
  },
  price: {
    whiteSpace: 'nowrap'
  },
  value: {
    color: colors.green[600],
    fontWeight: theme.typography.fontWeightMedium
  },
  conversion: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end'
  },
  conversionStats: {
    whiteSpace: 'nowrap',
    marginRight: theme.spacing(2)
  },
  actions: {
    justifyContent: 'flex-end'
  },
  arrowForwardIcon: {
    marginLeft: theme.spacing(1)
  }
}));

const ListUsers = props => {
  const { className, title, users, ...rest } = props;

  const classes = useStyles();

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <CardHeader
        action={<GenericMoreButton />}
        title={title}
      />
      <Divider />
      <CardContent className={classes.content}>
        <PerfectScrollbar>
          <div className={classes.inner}>
            <Table>
              <TableBody>
                {users.map(users => (
                  <TableRow
                    hover
                    key={users.user.id}
                  >
                    <TableCell>
                      <div className={classes.details}>
                        <img
                          alt="User"
                          className={classes.image}
                          src="/images/products/product_freelancer.svg"
                        />
                        <div>
                          <Typography variant="h6">{users.user.name}</Typography>
                          <Typography variant="subtitle2">
                            <span className={classes.subscriptions}>
                              {users.user.user_name}
                            </span>
                          </Typography>
                        </div>
                      </div>
                    </TableCell>
                    <TableCell>
                      <Typography variant="h6">Sale</Typography>
                      <Typography
                        className={classes.sale}
                        variant="subtitle2"
                      >
                        <span className={classes.value}>
                          {'$ '}{users.sale}
                        </span>
                      </Typography>
                    </TableCell>                    
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </PerfectScrollbar>
      </CardContent>
      <Divider />
      <CardActions className={classes.actions} />
    </Card>
  );
};

ListUsers.propTypes = {
  className: PropTypes.string,
  title: PropTypes.string,
  users: PropTypes.array
};

export default ListUsers;
