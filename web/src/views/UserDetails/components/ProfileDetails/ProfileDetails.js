import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardContent,
  Avatar,
  Typography
} from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  root: {},
  content: {
    display: 'flex',
    alignItems: 'center',
    flexDirection: 'column',
    textAlgin: 'center'
  },
  name: {
    marginTop: theme.spacing(1)
  },
  avatar: {
    height: 100,
    width: 100
  },
  removeBotton: {
    width: '100%'
  }
}));

const ProfileDetails = props => {
  const { profile, className, sales, ...rest } = props;

  const classes = useStyles();

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <CardContent className={classes.content}>
        <Avatar
          className={classes.avatar}
          src="/images/products/product_freelancer.svg"
        />
        <Typography
          className={classes.name}
          gutterBottom
          variant="h3"
        >
          {profile.name}
        </Typography>
        <Typography
          color="textSecondary"
          variant="body1"
        >
          {profile.user_name}
        </Typography>
        <Typography
          color="textSecondary"
          variant="body2"
        >
          {profile.phone}
        </Typography>
        <Typography
          color="textSecondary"
          variant="body2"
        >
          {'$ '}{sales}
        </Typography>
      </CardContent>      
    </Card>
  );
};

ProfileDetails.propTypes = {
  className: PropTypes.string,
  profile: PropTypes.object.isRequired,
  sales: PropTypes.number
};

export default ProfileDetails;
